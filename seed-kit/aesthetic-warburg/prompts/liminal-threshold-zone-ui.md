---
type: prompt
slug: liminal-threshold-zone-ui
modality: ui
pathosformel: "[[liminal-threshold-zone]]"
aat: "AAT:UNKNOWN — verify at aat.getty.edu (candidate 300056497 transitional spaces)"
iconclass: "UNKNOWN — verify at iconclass.org (candidate 22A threshold / boundary)"
schema_version: 2.1.0
---

# Liminal Threshold Zone — UI surface (阈限地带作为界面过渡)

## Subject
A transitional interface state — loading, authenticating, entering a new context, crossing from public to private area.
Content from the outgoing context is still partially present; content from the incoming context is partially arrived.
The rules of interaction are briefly suspended: no primary CTA is offered during the threshold; the user cannot advance until the crossing resolves.
The surface is not a spinner, not a progress bar — it is a held moment.

## Style
Tarkovsky 1979 (Stalker, Zone crossing at the fence) as the authoritative liminal form / Lynch 1990–91 (Twin Peaks Red Room) and 2017 (Twin Peaks: The Return episode 8) as its mass-media inheritance / Garland 2018 (Annihilation Shimmer) as its contemporary digital-age variant.
The lineage test: the user is crossing a boundary; the UI honors that the crossing takes time and changes the viewer, not just the screen.

## Composition
Asymmetric split: outgoing-context region occupies one edge of the viewport at reduced opacity (0.3–0.5); incoming-context region begins to assemble from the opposite edge.
A vertical or diagonal soft-edged boundary bisects the two — not a hard line, a gradient band 80–160px wide where the regions interpenetrate.
No primary action is visible inside the boundary band.
Color key: outgoing region at its own scheme, incoming region shifted -5 lightness and +8 chroma on the hue axis — slightly alien.

## Motion
The boundary band drifts slowly across the viewport (2–5 seconds) to sweep the crossing. Within the band, content elements refract — a subtle displacement map or oklch hue shift, not a blur.
On reduced-motion: the drift becomes a single crossfade of identical duration.
Interaction during the crossing is disabled but clearly temporary — the cursor reads "waiting," not "broken."

## Notes
Do NOT generate: loading spinners, indeterminate progress bars, skeleton screens with shimmer gradients, splash screens with logo animations, generic fade-to-black transitions, dissolve effects borrowed from iOS defaults, page-flip metaphors. This Pathosformel treats the threshold as a real state the user passes through — if the transition is incidental chrome, the form is broken.
