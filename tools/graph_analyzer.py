#!/usr/bin/env python3
"""Graph intelligence for Bab-ilu vault — builds wiki/_insights.md.

Reads vault MD frontmatter + body wikilinks, constructs a networkx graph,
computes topology metrics, and writes a human-readable `_insights.md`
(Karpathy primitive for self-evolving LLM Wiki, v2.1 lens-parameterized).

Metrics computed:
  - Topic clusters (Louvain community detection, resolution + random_state
    sourced from `lens.community_detection`)
  - Bridge nodes (betweenness centrality top 10)
  - Content gaps (disconnected communities + empty domains + missing anchors)
  - Structural bias (domain distribution, era distribution, confidence)
  - Anchor health (authority-field fill rate, fields from `lens.anchors`)

v2.1 change (D1): every hardcoded aesthetic-warburg assumption
(tier-0 type `"aesthetic"`, tier-1 cluster type `"panel"`, authority
field list, domain set, thresholds) now flows from a `LensConfig`.
Pass `--lens <id>` to select, or rely on `.agent/lenses/active/` when
`/genesis` has activated one.

Usage:
    python3 tools/graph_analyzer.py --lens aesthetic-warburg
    python3 tools/graph_analyzer.py                   # uses active lens
    python3 tools/graph_analyzer.py --dry-run
    python3 tools/graph_analyzer.py --vault PATH --lens engineering-alexander
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from typing import Any

try:
    import networkx as nx
except ImportError:
    print("error: networkx required · pip install networkx>=3.3", file=sys.stderr)
    sys.exit(2)

try:
    import community as community_louvain
except ImportError:
    print("error: python-louvain required · pip install python-louvain", file=sys.stderr)
    sys.exit(2)

try:
    from lens_loader import LensConfig, LensValidationError, load_lens
except ImportError:  # tools/ also importable as a package (`python -m tools.graph_analyzer`)
    from tools.lens_loader import LensConfig, LensValidationError, load_lens  # type: ignore[no-redef]

REPO = Path(__file__).resolve().parents[1]
# Default to the current working directory. Tools invoked from a vault
# will find it automatically; tools invoked from elsewhere should pass
# --vault explicitly. Prior versions hardcoded the author's personal
# path (Documents/Bab-ilu), which masked "works on my machine" bugs
# by silently reading a vault no one else had.
DEFAULT_VAULT = Path.cwd()


def _validate_vault_or_exit(vault_path: Path) -> Path:
    """Fail fast if `vault_path` does not look like a Bab-ilu vault.

    A Bab-ilu vault has `.agent/` (lens configs) or `wiki/` (LLM-written
    content) at its root. The prior behaviour silently accepted any
    directory — which masked "works on my machine" bugs. Now we error
    clearly so the user sees the problem immediately.
    """
    vault_path = vault_path.resolve()
    has_agent = (vault_path / ".agent").is_dir()
    has_wiki = (vault_path / "wiki").is_dir()
    if not (has_agent or has_wiki):
        import sys as _sys
        print(
            f"error: {vault_path} does not look like a Bab-ilu vault "
            f"(no .agent/ or wiki/ subdirectory). Pass --vault <path> "
            f"explicitly or run this command from a vault root.",
            file=_sys.stderr,
        )
        _sys.exit(2)
    return vault_path
DEFAULT_LENSES_BASE = REPO / ".agent" / "lenses"
ACTIVE_LENS_DIRNAME = "active"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+?)(?:[|#][^\]]*)?\]\]")
RELATION_RE = re.compile(r"\{?\s*type:\s*(\w+)\s*,\s*target:\s*\[?\[?\[?([^\]\}]+?)\]?\]?\]?\s*\}?")


def _authority_fields(lens: LensConfig) -> list[str]:
    """Extract authority field list from `lens.anchors`, or return [] if
    the lens declares none. An empty list disables anchor-health checks
    gracefully — zettelkasten-style lenses don't need external IDs."""
    if lens.anchors is None:
        return []
    raw = lens.anchors.get("authority_fields", [])
    return list(raw) if raw else []


def parse_frontmatter(text: str) -> dict[str, Any] | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm = m.group(1)
    out: dict[str, Any] = {}
    current_key: str | None = None
    for line in fm.split("\n"):
        if not line.strip():
            continue
        top = re.match(r"^([\w_-]+):\s*(.*)$", line)
        if top:
            key, val = top.group(1), top.group(2).strip()
            if val == "":
                out[key] = []
                current_key = key
            else:
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                if val == "null":
                    val_parsed: Any = None
                elif val in ("true", "false"):
                    val_parsed = val == "true"
                else:
                    try:
                        val_parsed = int(val)
                    except ValueError:
                        try:
                            val_parsed = float(val)
                        except ValueError:
                            val_parsed = val
                out[key] = val_parsed
                current_key = None
        elif current_key and line.startswith(("  ", "\t", "- ")):
            if isinstance(out.get(current_key), list):
                out[current_key].append(line.strip().lstrip("- "))
    return out


def load_wiki(vault: Path) -> dict[str, dict]:
    """Scan wiki/ for all MD files, return {slug: {path, frontmatter, wikilinks}}."""
    wiki = vault / "wiki"
    nodes: dict[str, dict] = {}
    for md_path in wiki.rglob("*.md"):
        if md_path.is_symlink():
            continue
        if md_path.name.startswith("."):
            continue
        try:
            text = md_path.read_text(encoding="utf-8")
        except Exception:
            continue
        fm = parse_frontmatter(text) or {}
        slug = md_path.stem
        body = text[FRONTMATTER_RE.match(text).end():] if FRONTMATTER_RE.match(text) else text
        wikilinks = set()
        for m in WIKILINK_RE.finditer(body):
            tgt = m.group(1).strip()
            tgt = tgt.split("/")[-1]
            wikilinks.add(tgt)
        rel_block = re.search(r"^relations:\s*\n((?:\s+-.*\n?)+)", text, re.MULTILINE)
        relations = []
        if rel_block:
            for line in rel_block.group(1).split("\n"):
                m = RELATION_RE.search(line)
                if m:
                    relations.append({"type": m.group(1), "target": m.group(2).strip().strip("[]")})
        nodes[slug] = {
            "path": md_path,
            "relative_path": str(md_path.relative_to(vault)),
            "frontmatter": fm,
            "wikilinks": wikilinks,
            "relations": relations,
            "type": fm.get("type", "unknown"),
            "domain": fm.get("domain", None),
            "title": fm.get("title", slug),
        }
    return nodes


def build_graph(nodes: dict[str, dict]) -> nx.Graph:
    G = nx.Graph()
    for slug, data in nodes.items():
        G.add_node(slug, **{k: v for k, v in data.items() if k in ("type", "domain", "title")})
    for slug, data in nodes.items():
        for link in data["wikilinks"]:
            if link in nodes:
                G.add_edge(slug, link, via="wikilink")
        for rel in data["relations"]:
            if rel["target"] in nodes:
                G.add_edge(slug, rel["target"], via="relation", relation_type=rel["type"])
    return G


def compute_clusters(G: nx.Graph, *, lens: LensConfig) -> dict[str, int]:
    """Louvain community detection using lens's `resolution` + `random_state`."""
    if G.number_of_edges() == 0:
        return {n: 0 for n in G.nodes()}
    cd = lens.community_detection
    return community_louvain.best_partition(
        G,
        resolution=float(cd.get("resolution", 1.0)),
        random_state=int(cd.get("random_state", 42)),
    )


def compute_bridges(G: nx.Graph, top_k: int = 10) -> list[tuple[str, float]]:
    """Top-k bridge nodes by betweenness centrality. Lens-independent."""
    if G.number_of_nodes() < 3:
        return []
    bc = nx.betweenness_centrality(G)
    return sorted(bc.items(), key=lambda x: -x[1])[:top_k]


def detect_gaps(
    G: nx.Graph,
    nodes: dict[str, dict],
    clusters: dict[str, int],
    *,
    lens: LensConfig,
) -> list[dict]:
    """Identify high-priority content gaps under the given lens."""
    gaps: list[dict] = []
    tier_0 = lens.entity_model["tier_0"]
    tier_1_cluster = lens.entity_model["tier_1_cluster"]
    thresholds = lens.thresholds
    cluster_member_min = int(thresholds.get("cluster_member_min", 3))
    domain_min = int(thresholds.get("domain_min", 3))
    orphan_min_degree = int(thresholds.get("orphan_min_degree", 1))
    cluster_min_size = int(thresholds.get("cluster_min_size", 3))
    authority_fields = _authority_fields(lens)

    # Gap 1: Domains with < domain_min tier-0 entries
    domain_counts: Counter = Counter()
    for slug, data in nodes.items():
        if data["type"] == tier_0 and data.get("domain"):
            domain_counts[data["domain"]] += 1
    lens_domains = set(lens.allowed_subdomains)
    for dom in lens_domains:
        count = domain_counts.get(dom, 0)
        if count < domain_min:
            gaps.append({
                "priority": "high" if count == 0 else "medium",
                "kind": "underpopulated_domain",
                "target": dom,
                "current": count,
                "minimum": domain_min,
                "suggestion": (
                    f"域 `{dom}` 只有 {count} 张 {tier_0} 卡（<{domain_min}）。"
                    f"补强建议：扫 `_refs/_domains/{dom}.md` 挑 2-3 位作者做种子"
                ),
            })

    # Gap 2: tier-1 clusters with < cluster_member_min members
    for slug, data in nodes.items():
        if data["type"] != tier_1_cluster:
            continue
        member_count = (
            sum(1 for rel in data["relations"] if rel["type"] == "exemplifies")
            + len([n for n in G.neighbors(slug) if nodes.get(n, {}).get("type") == tier_0])
        )
        if member_count < cluster_member_min:
            gaps.append({
                "priority": "medium",
                "kind": f"understaffed_{tier_1_cluster}",
                "target": slug,
                "current": member_count,
                "minimum": cluster_member_min,
                "suggestion": (
                    f"{tier_1_cluster} [[{slug}]] 成员 {member_count}（<{cluster_member_min}）。"
                    f"考虑补成员或标 `incomplete`"
                ),
            })

    # Gap 3: Orphan tier-0 nodes
    for slug, data in nodes.items():
        if data["type"] != tier_0:
            continue
        degree = G.degree(slug)
        if degree <= orphan_min_degree:
            gaps.append({
                "priority": "low",
                "kind": f"orphan_{tier_0}",
                "target": slug,
                "degree": degree,
                "suggestion": (
                    f"[[{slug}]] 度数 {degree}，几乎无连接。"
                    f"考虑加关联字段或用 `/cross-link` 找潜在关联"
                ),
            })

    # Gap 4: Nodes missing authoritative anchor
    if authority_fields:
        anchor_scope = {tier_0, tier_1_cluster}
        for slug, data in nodes.items():
            if data["type"] not in anchor_scope:
                continue
            fm = data["frontmatter"]
            has_anchor = any(fm.get(f) not in (None, "", "null") for f in authority_fields)
            if not has_anchor:
                fields_hint = " / ".join(authority_fields[:4])
                gaps.append({
                    "priority": "high",
                    "kind": "missing_authority_anchor",
                    "target": slug,
                    "suggestion": (
                        f"[[{slug}]] 所有权威字段（{fields_hint}…）全空，"
                        f"违反 {lens.id} schema 硬规则"
                    ),
                })

    # Gap 5: Disconnected cluster pairs (size-gated)
    if len(set(clusters.values())) > 1:
        cluster_of = clusters
        cluster_members: dict[int, list[str]] = defaultdict(list)
        for n, c in cluster_of.items():
            cluster_members[c].append(n)
        pairs_connected: set[tuple[int, int]] = set()
        for u, v in G.edges():
            cu, cv = cluster_of.get(u), cluster_of.get(v)
            if cu is not None and cv is not None and cu != cv:
                pair = tuple(sorted([cu, cv]))
                pairs_connected.add(pair)
        all_cluster_ids = sorted(cluster_members.keys())
        for i in all_cluster_ids:
            for j in all_cluster_ids:
                if i >= j:
                    continue
                if (i, j) not in pairs_connected:
                    ex_i = cluster_members[i][0] if cluster_members[i] else "?"
                    ex_j = cluster_members[j][0] if cluster_members[j] else "?"
                    if (
                        len(cluster_members[i]) < cluster_min_size - 1
                        or len(cluster_members[j]) < cluster_min_size - 1
                    ):
                        continue
                    gaps.append({
                        "priority": "medium",
                        "kind": "disconnected_clusters",
                        "source_cluster": i,
                        "target_cluster": j,
                        "example_members": [ex_i, ex_j],
                        "suggestion": (
                            f"Cluster {i} 与 {j} 无连接（示例：[[{ex_i}]] / [[{ex_j}]]）。"
                            f"考虑桥接 {tier_1_cluster} 或交叉引用"
                        ),
                    })

    return gaps


def compute_structural_bias(
    nodes: dict[str, dict], *, lens: LensConfig
) -> dict:
    """Domain / time / confidence distribution over tier-0 entries."""
    tier_0 = lens.entity_model["tier_0"]
    domain_counts: Counter = Counter()
    era_counts: Counter = Counter()
    confidences: list[float] = []
    for slug, data in nodes.items():
        if data["type"] != tier_0:
            continue
        if data.get("domain"):
            domain_counts[data["domain"]] += 1
        conf = data["frontmatter"].get("confidence")
        if isinstance(conf, (int, float)):
            confidences.append(conf)
        title = data.get("title", "")
        for m in re.finditer(r"\b(1[5-9]\d\d|20[0-2]\d)\b", title + " " + str(data["frontmatter"].get("aliases", ""))):
            y = int(m.group(1))
            era = f"{y // 100}c"
            era_counts[era] += 1
            break
    return {
        "domain_distribution": dict(domain_counts),
        "era_distribution": dict(era_counts),
        "avg_confidence": round(sum(confidences) / len(confidences), 3) if confidences else None,
        "total_tier_0": sum(1 for d in nodes.values() if d["type"] == tier_0),
    }


def render_insights(
    G: nx.Graph,
    nodes: dict[str, dict],
    clusters: dict[str, int],
    bridges: list[tuple[str, float]],
    gaps: list[dict],
    bias: dict,
    *,
    lens: LensConfig,
) -> str:
    today = date.today().isoformat()
    tier_0 = lens.entity_model["tier_0"]
    tier_1_cluster = lens.entity_model["tier_1_cluster"]
    cluster_members: dict[int, list[str]] = defaultdict(list)
    for n, c in clusters.items():
        cluster_members[c].append(n)
    sorted_clusters = sorted(cluster_members.items(), key=lambda x: -len(x[1]))
    authority_fields = _authority_fields(lens)

    lines = [
        "---",
        "id: wiki-insights",
        "type: concept",
        "role: foundation",
        "title: Bab-ilu Wiki Insights (graph intelligence)",
        (
            f"description: Auto-generated by tools/graph_analyzer.py under lens "
            f"'{lens.id}' — topic clusters, bridge nodes, content gaps, "
            f"structural bias. Karpathy primitive for self-evolving LLM Wiki."
        ),
        f"lens: {lens.id}",
        "llm_owned: true",
        f"created: {today}",
        f"updated: {today}",
        'schema_version: "2.1.0"',
        "---",
        "",
        "# Wiki Insights (graph intelligence)",
        "",
        f"> 自动生成 · {today} · lens={lens.id} · 节点 {G.number_of_nodes()} · 边 {G.number_of_edges()}",
        "",
        "## 1. Topic Clusters (Louvain)",
        "",
        f"Vault 的 {G.number_of_nodes()} 个节点自发聚合为 {len(cluster_members)} 个簇。",
        "",
    ]
    for cid, members in sorted_clusters[:8]:
        if len(members) < 2:
            continue
        top_member = members[0]
        top_title = nodes.get(top_member, {}).get("title", top_member)
        lines.append(f"- **Cluster {cid}** ({len(members)} 成员) · 代表 [[{top_member}]] ({top_title})")
        sample = ", ".join(f"[[{m}]]" for m in members[:6])
        lines.append(f"  成员: {sample}" + (" …" if len(members) > 6 else ""))
    if any(len(m) < 2 for m in cluster_members.values()):
        singletons = sum(1 for m in cluster_members.values() if len(m) < 2)
        lines.append(f"- **孤节点** × {singletons}（未聚合成簇）")

    lines += [
        "",
        "## 2. Bridge Nodes (betweenness centrality top 10)",
        "",
        "连接多个 cluster 的「枢纽」节点。它们最具「跨域引用」价值。",
        "",
    ]
    if bridges:
        for i, (node, score) in enumerate(bridges, 1):
            if score < 0.001:
                continue
            title = nodes.get(node, {}).get("title", node)
            lines.append(f"{i}. [[{node}]] — {title} (bc={score:.3f})")
    else:
        lines.append("_(graph 过小或无边，betweenness 不具代表性)_")

    lines += [
        "",
        "## 3. Content Gaps (auto-detected)",
        "",
        "**这是 `/gap` 的数据源**。优先级高的 gap 应在下一轮 /taste / /research 循环处理。",
        "",
    ]
    by_priority = defaultdict(list)
    for g in gaps:
        by_priority[g["priority"]].append(g)
    for pri in ["high", "medium", "low"]:
        items = by_priority.get(pri, [])
        if not items:
            continue
        lines.append(f"### Priority: {pri}")
        lines.append("")
        for g in items[:10]:
            lines.append(f"- **{g['kind']}** · {g['suggestion']}")
        if len(items) > 10:
            lines.append(f"- _… 省略 {len(items) - 10} 条同优先级 gap_")
        lines.append("")

    lines += [
        "## 4. Structural Bias",
        "",
        f"**域分布（tier-0 = {tier_0}）:**",
        "",
    ]
    total_t0 = bias["total_tier_0"]
    for dom, cnt in sorted(bias["domain_distribution"].items(), key=lambda x: -x[1]):
        pct = round(cnt * 100 / total_t0, 1) if total_t0 else 0
        lines.append(f"- `{dom}`: {cnt} ({pct}%)")
    lens_domains = set(lens.allowed_subdomains)
    missing = lens_domains - set(bias["domain_distribution"])
    if missing:
        lines.append(f"- _缺失域_: {', '.join(sorted(missing))}")

    lines += [
        "",
        "**时代分布（推断自标题 / 别名）:**",
        "",
    ]
    if bias["era_distribution"]:
        for era, cnt in sorted(bias["era_distribution"].items()):
            lines.append(f"- `{era}`: {cnt}")
    else:
        lines.append("_(无可推断时代信息)_")

    lines += [
        "",
        f"**平均 confidence**: {bias['avg_confidence'] or '(no data)'}",
        "",
        "## 5. Authority Anchor Health",
        "",
    ]
    if authority_fields:
        anchor_scope = {tier_0, tier_1_cluster}
        anchor_missing = [
            slug for slug, data in nodes.items()
            if data["type"] in anchor_scope
            and not any(data["frontmatter"].get(f) not in (None, "", "null") for f in authority_fields)
        ]
        total_nodes_requiring = sum(1 for d in nodes.values() if d["type"] in anchor_scope)
        compliant = total_nodes_requiring - len(anchor_missing)
        pct = round(compliant * 100 / total_nodes_requiring, 1) if total_nodes_requiring else 100
        lines.append(
            f"- 合规率: {compliant}/{total_nodes_requiring} ({pct}%) 满足 {lens.id} 锚点规则"
        )
        if anchor_missing:
            lines.append(f"- 违规节点 ({len(anchor_missing)}):")
            for slug in anchor_missing[:10]:
                lines.append(f"  - [[{slug}]]")
            if len(anchor_missing) > 10:
                lines.append(f"  - _… 省略 {len(anchor_missing) - 10} 条_")
    else:
        lines.append(f"_(lens `{lens.id}` 未声明 authority_fields — 本节省略)_")

    lines += [
        "",
        "---",
        "",
        "## 维护",
        "",
        f"- `python3 tools/graph_analyzer.py --lens {lens.id}` 重新生成本文件",
        "- `/gap --dry-run` 读取 §3 gaps 列 top 3",
        "- `/gap --take <N>` 接受第 N 条建议并自动执行",
        "- `/lint` 会验证本文件与 vault 当前状态的 drift",
        "",
        f"_最后更新: {today}_",
    ]
    return "\n".join(lines) + "\n"


def _resolve_lens(args: argparse.Namespace) -> LensConfig:
    """Pick the lens to run under. Precedence: --lens > active/lens.yaml.

    Lens-base precedence (round-5 audit fix): explicit --lenses-base
    wins; otherwise prefer `<args.vault>/.agent/lenses/` if it exists;
    otherwise fall back to the repo-relative `DEFAULT_LENSES_BASE`.
    This lets users on foreign vaults (outside the repo checkout)
    resolve their own lens config — previously the --vault flag was
    surface-only and lens-base stayed hardcoded to the installed repo.

    Never silently falls back to aesthetic-warburg — v2.1 explicitly
    requires an activated lens (PRD §6.1) so ambiguous runs fail loudly.
    """
    if args.lenses_base:
        base = Path(args.lenses_base)
    else:
        vault_lens_base = Path(args.vault).resolve() / ".agent" / "lenses"
        if vault_lens_base.is_dir():
            base = vault_lens_base
        else:
            base = DEFAULT_LENSES_BASE
    if args.lens:
        try:
            return load_lens(args.lens, base=base)
        except (FileNotFoundError, LensValidationError) as exc:
            print(f"error: lens '{args.lens}' could not be loaded: {exc}", file=sys.stderr)
            sys.exit(2)
    active_dir = base / ACTIVE_LENS_DIRNAME
    active_file = active_dir / "lens.yaml"
    if not active_file.exists():
        # Distinguish: (a) no active pointer at all vs (b) active is a
        # symlink whose target was deleted. Path.exists() returns False
        # for both, but the fix for each is different: (a) run /genesis,
        # (b) re-point the symlink. The dangling-symlink check has to
        # target the *parent* `active` directory/link itself, because
        # once the target is gone `active/lens.yaml` is not itself a
        # symlink — `active` is. Prior revisions called
        # active_file.is_symlink() which returned False for this case
        # and silently routed everyone to error (a).
        if active_dir.is_symlink():
            link_target = None
            try:
                link_target = active_dir.readlink()  # py3.9+
            except OSError:
                pass
            print(
                f"error: {active_dir} is a broken symlink"
                + (f" pointing at '{link_target}'" if link_target else "")
                + " — target missing. Re-point it to an existing lens dir "
                + f"under {base} (run /genesis to rebuild, or `ln -sfn "
                + f"<lens-id> {active_dir}` manually).",
                file=sys.stderr,
            )
        else:
            print(
                f"error: no --lens given and no active lens at {active_file}. "
                f"Run /genesis to activate one, or pass --lens <id>.",
                file=sys.stderr,
            )
        sys.exit(2)
    # active/ is a pointer copy; read the id field to locate the source dir
    # (per /genesis protocol, .agent/lenses/<id>/ always exists alongside).
    try:
        import yaml
        active_yaml = yaml.safe_load(active_file.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        print(f"error: could not parse {active_file}: {exc}", file=sys.stderr)
        sys.exit(2)
    active_id = active_yaml.get("id")
    if not isinstance(active_id, str) or not active_id:
        print(f"error: {active_file} missing 'id' field", file=sys.stderr)
        sys.exit(2)
    try:
        return load_lens(active_id, base=base)
    except (FileNotFoundError, LensValidationError) as exc:
        print(
            f"error: active lens '{active_id}' source dir not found: {exc}",
            file=sys.stderr,
        )
        sys.exit(2)


def _run_pipeline(args: argparse.Namespace, lens: LensConfig) -> None:
    """Main pipeline: scan → graph → cluster → gaps → render → write.

    Split out from main() so tests can monkeypatch around filesystem work
    while still exercising the lens-resolution branch.

    main() already called _validate_vault_or_exit before resolving the
    lens (Wave 9 ordering fix). We do NOT re-validate here — duplicate
    validation was removed when round-8 audit flagged it as redundant
    dead code at line 641 of the prior revision.
    """
    vault = Path(args.vault).resolve()
    if not (vault / "wiki").is_dir():
        print(f"error: no wiki/ in {vault}", file=sys.stderr)
        sys.exit(2)

    print(f"scanning {vault}/wiki/ (lens={lens.id})", file=sys.stderr)
    nodes = load_wiki(vault)
    print(f"  loaded {len(nodes)} MDs", file=sys.stderr)

    G = build_graph(nodes)
    print(f"  graph: {G.number_of_nodes()} nodes · {G.number_of_edges()} edges", file=sys.stderr)

    clusters = compute_clusters(G, lens=lens)
    print(f"  clusters: {len(set(clusters.values()))}", file=sys.stderr)

    bridges = compute_bridges(G)
    print(f"  bridge nodes (top with bc>0): {sum(1 for _, s in bridges if s > 0)}", file=sys.stderr)

    gaps = detect_gaps(G, nodes, clusters, lens=lens)
    print(f"  gaps: {len(gaps)} (high={sum(1 for g in gaps if g['priority']=='high')})", file=sys.stderr)

    bias = compute_structural_bias(nodes, lens=lens)
    insights_md = render_insights(G, nodes, clusters, bridges, gaps, bias, lens=lens)

    if args.dry_run:
        print(insights_md)
    else:
        out_path = vault / "wiki" / "_insights.md"
        out_path.write_text(insights_md, encoding="utf-8")
        print(f"✓ wrote {out_path.relative_to(vault)}", file=sys.stderr)

    if args.json:
        json_out = {
            "generated": date.today().isoformat(),
            "lens": lens.id,
            "nodes": G.number_of_nodes(),
            "edges": G.number_of_edges(),
            "clusters": dict(Counter(clusters.values())),
            "bridges": [{"node": n, "bc": round(s, 4)} for n, s in bridges if s > 0],
            "gaps": gaps,
            "bias": bias,
        }
        jpath = vault / "wiki" / "_index" / "insights.json"
        jpath.parent.mkdir(exist_ok=True)
        jpath.write_text(json.dumps(json_out, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"✓ wrote {jpath.relative_to(vault)}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="Print to stdout only, don't write _insights.md")
    ap.add_argument("--vault", default=str(DEFAULT_VAULT))
    ap.add_argument("--json", action="store_true", help="Emit machine-readable JSON alongside")
    ap.add_argument("--lens", default=None, help="Lens id (default: read .agent/lenses/active/)")
    ap.add_argument(
        "--lenses-base",
        default=None,
        help=f"Directory containing lens dirs (default: {DEFAULT_LENSES_BASE})",
    )
    args = ap.parse_args()

    # Vault validation first: if the user passed a non-vault --vault,
    # don't confuse them with a lens-resolution error that points at
    # the repo path instead of the path they typed. Parallel to the
    # ordering fix applied to ingest_runner + gap_runner.
    _validate_vault_or_exit(Path(args.vault))
    lens = _resolve_lens(args)
    _run_pipeline(args, lens)


if __name__ == "__main__":
    main()
