# Bab-ilu

**You bring the material and the questions. The LLM does every bit of bookkeeping.**

The books you read, papers you scan, references you save, thinking notes you scribble — scattered across twenty Notion pages, markdown files, and drafts, none of them aware of each other. Bab-ilu lets Claude assemble them locally into **a knowledge base that grows itself**. You never write a wikilink, never maintain a cross-reference, never tidy a directory.

Inspired by Andrej Karpathy's [LLM-Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): *"The tedious part of a knowledge base is the bookkeeping, and LLMs are best at bookkeeping."* Bab-ilu is an implementation of that idea, plus two useful extensions Karpathy's gist doesn't cover (see below).

> ⚠️ **v2.2 alpha.** Architecture stable; details may still shift. Runs locally; your material never leaves your machine.
> *[中文 →](README.md)*

---

## What a typical session looks like

Over the past month you read two books and took notes: Schön's *The Reflective Practitioner* and Sennett's *The Craftsman*. The notes sit in a few markdown files. The concepts between them were never connected.

You open Claude Code in the project root:

```text
you:     /ingest book-notes/
Claude:  Read 2 note files. Created one source entry per book. Extracted
         7 concepts (knowing-in-action / tacit-knowledge / craft-as-dialogue / …)
         and built wikilinks. The two books share 3 concepts; auto-linked.

you:     /ask How do these two books complement each other on how experts think?
Claude:  [a 600-word synthesis with specific citations]
         Archive this synthesis as a new wiki page? (Y/n)
you:     y

(You keep reading. A week later you ingest 3 more note files.)

you:     /gap
Claude:  Spotted a concept cluster (expert knowledge / tacit skill / reflection)
         with no explicit link to another cluster (craft practice / apprenticeship
         models), though both reference Sennett twice. Want to add a bridge?

you:     /evolve-lens
Claude:  I notice your last three months of notes keep circling "how experts
         think in action." That's structurally isomorphic to Donald Schön's
         1983 The Reflective Practitioner — the knowing-in-action /
         reflection-in-action / reflection-on-action three-layer framework.
         Install a schon-reflective-practice lens so new notes auto-sort into
         those layers?
```

**Outcome**: you wrote no markdown, maintained no wikilinks, drew no mind map. Claude did all the bookkeeping. You kept the decisions — what to read, what to ask, what to accept.

---

## If you work in visual creation

Film, design, architecture, illustration, game concept art — Bab-ilu ships a deep-polished lens made for you, called **aesthetic-warburg**. Two people are its bones:

**Aby Warburg** (1866–1929) was the eldest son of a Hamburg banker. On the day he came of age, he told his younger brother: *"Take the family business. I'll spend my life buying books, and you'll pay the bill."* He lived that trade out. He left behind a Kulturwissenschaftliche Bibliothek of tens of thousands of volumes (today still operating, in London, as The Warburg Institute), and an unfinished final work — the *Bilderatlas Mnemosyne*: nearly a thousand photographs and images, juxtaposed on sixty-three black panels, **with no captions at all**. Visual resonance alone was meant to let the viewer see — that a Greek dancer's posture, a Renaissance biblical illumination, a nineteenth-century postage stamp, and a contemporary Michelin tire advertisement **carry the same "emotional formula" (Pathosformel), reincarnated in different vessels across two millennia (Nachleben)**. Warburg believed images could speak to each other directly — if you placed them close enough, in sufficient numbers.

**Erwin Panofsky** (1892–1968) was Warburg's young colleague in Hamburg, later driven out of Germany by the Nazis. At the Princeton Institute for Advanced Study he refined Warburg's intuitions into a rigorous analytical framework. His 1939 *Studies in Iconology* proposed reading an image in three layers: first what it is as formal fact (pre-iconographic), then what cultural stories it carries (iconographic), then what worldview of an era leaks through it (iconological). These three layers are today the foundational course in every art-history graduate program on earth.

Between them, they pushed the craft of **systematically reading a single image, and tracing a visual motif's migration across eras**, to the highest point humans have reached. **Bab-ilu invents no new method — it just wires theirs into the LLM loop.** What you're about to see as `/taste`'s three-layer output is Panofsky's 1939 framework. The Pathosformel / Nachleben / Mnemosyne Panel you'll encounter — those are Warburg's own terms.

Drop in a film still, a painting, a concept-art piece:

```text
you:    /taste raw/images/blade-runner-2049-orange-void.jpg
Claude:
  【Pre-iconographic layer】
    A single back-turned figure in a vast orange atmosphere, on a
    barren horizontal ground. Composition: lone mid-shot slightly
    right of center; horizon at lower 2/3; radically unified color
    temperature.

  【Iconographic layer】
    "Rückenfigur" (back-turned figure) — the German Romantic formula
    established in Caspar David Friedrich's Monk by the Sea (1808):
    a single figure faces the infinite; the viewer looks out over
    their shoulder. Villeneuve reactivates this formula in Blade
    Runner 2049.

  【Iconological layer】
    This is a Warburg Pathosformel — a 200-year afterlife (Nachleben)
    of a "sublime solitude" affect formula. It doesn't carry specific
    Romantic iconography; it carries the *structural posture* of the
    individual-against-the-infinite. From Friedrich to Tarkovsky's
    Stalker to Villeneuve, the same formula lives inside different
    cultural vessels.

  Wrote wiki/motif/rueckenfigur-modern;
  Created wiki/panel/sublime-solitude-against-void as a Panel;
  Linked Nachleben references to friedrich-monk-by-sea and
  tarkovsky-stalker-zone source entries.

you:    /prompt rueckenfigur-modern ui
Claude:
  Generated a four-segment Midjourney prompt for the UI modality.
  Crucially, the prompt is **not a copy of any single source image**
  — it produces a new image that *sits inside the Pathosformel lineage*:
    Subject:     solitary figure, back-to-camera, slightly right of center...
    Style:       Rückenfigur tradition via Friedrich 1808 / Villeneuve 2017
    Composition: horizon at lower 2/3, atmospheric saturation, minimal foreground...
    Motion:      static-contemplative, faint breath of wind in garments
  Authority anchors: IMDB tt1856101 (Blade Runner 2049); Wikidata + Getty AAT
                     for the cross-media Rückenfigur motif, pulled from the
                     aesthetic-warburg seed-kit when present.

you:    /gap
Claude:
  The panel has 3 members so far (Friedrich / Tarkovsky / Villeneuve),
  all Western or Russian. The Pathosformel's East Asian variants
  (Edo-period distant-gaze in ukiyo-e, the staffage figure in Song-
  dynasty landscape) are not yet in the vault. Want me to generate a
  material-request?
```

Other lenses don't do this yet — not because the technology can't, but because Warburg's century of scholarship, Panofsky's three-layer framework, Getty's AAT / Iconclass / ULAN institutional anchor system, and a reverse-prompt pipeline that turns concepts into deployable generation prompts — all of these have to be wired in, one by one. Aesthetic was the first one finished, because visual analysis is the hardest case; other domains will follow.

---

## How is this different from just chatting with ChatGPT?

Chatting starts from scratch every time. Every insight you found, every cross-reference you traced, every note you organized — poof, gone when you close the tab.

Bab-ilu lets the LLM **write every insight into a persistent, cross-referenced local wiki**. Your knowledge **compounds** across uses. A year in, your vault is ten times thicker than a year ago — not because you worked harder, but because LLMs don't get tired of bookkeeping.

---

## Quick start

**Requirements**:
- Python 3.10+
- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) or Codex (Bab-ilu entrypoints run inside the agent conversation, not as shell commands: Claude Code uses `/genesis`-style slash commands, while Codex uses `$genesis`-style skill invocation; no `ANTHROPIC_API_KEY` — reasoning happens in the session)
- Any markdown editor (Obsidian / VSCode / whatever) to read the vault
- Codex users: see [docs/codex-quickstart.md](docs/codex-quickstart.md)

```bash
git clone https://github.com/<your-username>/bab-ilu.git
cd bab-ilu
pip install -r requirements.txt
```

Then open your agent runtime in this repo and enter the matching syntax:

```text
Claude Code:
/genesis
/ingest raw/your-stuff/
/ask "any natural-language question"

Codex:
$genesis
$ingest raw/your-stuff/
$ask "any natural-language question"
```

`/genesis` (or `$genesis` in Codex) asks 5 questions (vault language / pick a lens / work subdomain / demo seed? / ingest now?). Say yes to the demo seed and you get 3-5 example entries — enough to see how Bab-ilu works in 5 minutes.

---

## Workflow entrypoints

| Claude Code | Codex | What it does |
|---|---|---|
| `/genesis` | `$genesis` | Create a new vault |
| `/wx2md-worker <mp.weixin.qq.com URL>` | `$wx2md-worker <mp.weixin.qq.com URL>` | Capture a WeChat Official Account article into `raw/articles/` via worker before deciding whether to ingest it |
| `/ingest <path>` | `$ingest <path>` | Feed material: originals go to `raw/`; LLM analysis goes to `wiki/` |
| `/ask <question>` | `$ask <question>` | Query the vault in natural language; the answer can archive to `wiki/syntheses/` |
| `/gap` | `$gap` | Have Claude find missing links between concept clusters you haven't spotted |
| `/lint` | `$lint` | Vault health audit: contradictions, stale claims, missing material, orphan nodes |
| `/distill <source>` | `$distill <source>` | Re-structure foreign-language material into your schema (not translation) |
| `/prompt <entity>` | `$prompt <entity>` | Turn a concept or note into a deployable Midjourney / Sora prompt |
| `/taste <image>` | `$taste <image>` | Under aesthetic lens, runs full Panofsky three-layer creative analysis; under other lenses, falls back to that lens's diagnostic report mode |
| `/evolve-lens` | `$evolve-lens` | **Advanced**: let Claude propose a new cognitive framework drawn from your usage pattern |

---

## Advanced: grow a lens from your own usage

Bab-ilu has two layers of lenses with maturity tiers:

**Pre-installed mature lenses** (stress-test-verified, production-grade):

- **aesthetic-warburg** 🏛 **Flagship** — the one showcased above. Warburg's cross-epochal motif tracing + Panofsky's three-layer iconography + AAT/Iconclass/ULAN institutional anchors + Nachleben lineage + reverse-prompt pipeline. 47 seed-kit markdown files + 9-file reverse-prompt seed-kit. The most mature subsystem, and the project's "stress-test pass proof" — if Bab-ilu runs well on cross-millennium, cross-civilization, cross-symbolic-system visual art, other domains are easier.

**Pre-installed lenses: pipeline proven, seed-kit growing** (usable and documented; layered with working seed-kits; not yet polished to aesthetic-warburg's depth):

- **engineering-alexander** 🔧 — Christopher Alexander's pattern-language direction. 29 seed-kit markdown files + full lens.yaml/prompts.md/examples.md + 3-file reverse-prompt seed-kit (Context→Problem→Forces→Solution pattern cards), plus a dedicated `tools/incident_extractor.py` for URL and PDF postmortems. Fits engineers doing postmortems and decision logging.
- **general-zettelkasten** 📇 — Luhmann's card box method. 29 seed-kit markdown files + the full yaml/prompts.md/examples.md triad, 3-file progressive-summary seed-kit, plus a dedicated `tools/note_extractor.py` that handles URL/PDF/markdown/text inputs. Universal fallback; quick start for any discipline.

**Evolving layer**: the three won't cover everyone's work. So Bab-ilu has **LENS EVOLUTION**: a background observer that watches your actual behavior — what you ingest, what you ask, what you accept / reject — and when it recognizes that your real working pattern is structurally isomorphic to some **existing academic tradition with decades of scholarly backing** (Schön, Polanyi, Bourdieu, Merleau-Ponty, …), it proposes operationalizing that tradition as a new lens specifically for your vault.

**Key constraints**:
- No preset identity (no job-title gating — lawyers, doctors, researchers, creators all go through the same mechanism)
- Never invents a framework from thin air (candidates must be real traditions with 30+ year scholarly trails; an independent second LLM pass verifies the citation is real, not hallucinated)
- Never auto-installs (always proposes; you decide)

This is Bab-ilu's core extension over Karpathy's pattern: Karpathy lets the LLM do bookkeeping; Bab-ilu additionally lets the LLM **recognize which thinking framework you've been unconsciously using**.

---

## Three-layer architecture

```
raw/      your source material · immutable · Claude never touches it
wiki/     LLM-written, human-readable layer · markdown + wikilinks · any editor
.agent/   machine memory (graph, schema, lens config, observer state)
```

---

## FAQ

**Q: Do I have to use Obsidian?**
No. Bab-ilu requires no specific editor. The graph isn't for you to *look at* — you experience its emergence semantically through `/gap` / `/ask` / `/evolve-lens`, not by staring at nodes and edges. Obsidian / VSCode + Foam work if you want visualization, but nothing forces it.

**Q: Where does my material get uploaded?**
Nowhere. All reasoning runs inside the Claude Code session you started. The vault is markdown files on your machine; nothing leaves.

**Q: Isn't this only for visual-art people?**
Visual creators are the group who can **eat the deepest meal today** — the aesthetic (Warburg/Panofsky) lens is the most mature and feature-complete subsystem, immediately usable out of the box. But the project's goal is all domains. If you do engineering, research, writing, law, medicine, you start on `general-zettelkasten`, use it for a few weeks, and LENS EVOLUTION proposes a real-tradition academic lens specific to your discipline (Schön / Polanyi / Kuhn / IRAC — scholarly traditions with decades of backing). So: **visual creators eat today; other fields: use the generic first, grow your lens over weeks**.

**Q: Do I need to pay for API usage?**
No. All LLM reasoning runs natively in your Claude Code session; no outbound API calls; no `ANTHROPIC_API_KEY` required.

**Q: How is this related to Obsidian / Logseq / Notion?**
They're **reading/editing** tools. Bab-ilu is a **writing** tool — the LLM writes the wiki, builds wikilinks, composes synthesis. Use Bab-ilu to *produce* the vault; use Obsidian / Logseq / any editor to *read* it. No conflict.

---

## What Bab-ilu is not

- **Not a SaaS** — runs locally; material never leaves your machine
- **Not a search engine** — you don't "look things up"; you let material **grow structure**
- **Not a writing assistant** — it helps you *discover*; your own long-form writing lives in `wiki/my/` (a read-only namespace for the LLM)
- **Not something that needs an API key** — runs natively inside Claude Code

---

## The name

Bab-ilu is Akkadian *Bāb-ilu* — "Gate of the Gods," Babylon's original name. A nod at the project's ambition: **connecting concepts across languages, cultures, and domains** — the Babylon before the Tower, where the connection still works.

---

## Going deeper

Why the project is designed this way — its cybernetics + late-Wittgenstein theoretical foundation, the five operational principles, the §0.5 north-star claim — see [PRD-v2.1-zh.md](PRD-v2.1-zh.md) (Chinese; English translation planned).

Want to contribute / fix a bug / propose a lens candidate — see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

[MIT](LICENSE) · Copyright (c) 2026 Phoenix Ye and Bab-ilu contributors.

## Acknowledgments

This project stands on many shoulders.

Andrej Karpathy gave us the LLM-Wiki pattern — the raw / wiki / .agent three-layer skeleton is his. Aby Warburg taught images to speak to each other; Erwin Panofsky taught us how to listen — they are the root of the aesthetic lens. Christopher Alexander's *A Pattern Language* is the bone of the engineering lens. Niklas Luhmann's Zettelkasten is the method of the fallback lens.

**Special tribute to [skyllwt/OmegaWiki](https://github.com/skyllwt/OmegaWiki)** — Bab-ilu is its hard fork. The v1.x ingest / lint / check / graph loop, the skill-orchestration rhythm, the atomic-write and log-append discipline that actually work — OmegaWiki made all of that real first. v2.1's lens-aware rewrite only replaced that foundation's assumptions with a swappable lens layer. **Without OmegaWiki laying the groundwork, Bab-ilu would not have had a day one.** MIT-compatible licensing lets us acknowledge that inheritance honestly and in full view.

Full acknowledgments live in the PRD.
