---
type: prompt
slug: quiet-interior-light-ui
modality: ui
pathosformel: "[[quiet-interior-light]]"
aat: AAT:300056967 (interiors)
iconclass: 41A3 (interior of a house)
schema_version: 2.1.0
---

# Quiet Interior Light — UI surface (北面窗光作为界面光)

## Subject
A reading / writing / note-taking surface — single-column canvas, one active document, one persistent left-margin light source.
No avatars, no notifications stacked on top, no parallel chat rail.
The cursor is the only thing that moves until the user acts.
Whitespace around the content is load-bearing, not decorative.

## Style
Vermeer 1657 (Milkmaid) north-light domestic discipline / Hammershøi c.1900 (Interior) space-as-subject restraint / Deakins 2019 (1917 farmhouse dawn) cold-blue dawn palette carried into contemporary digital surface.
The lineage is: sacred-domestic window light → existential emptied window light → war-survivor shelter light — inherited as interface calm, not as stylistic flourish.

## Composition
Left-edge vertical light gradient (simulating a north window out of frame), 15–25% of viewport width, coolest at top.
Main content block offset from the light edge by a generous gutter — the gutter is the composition, not padding.
Fixed horizontal baseline grid so successive paragraphs breathe at the same cadence.
Color key: oklch(96% 0.008 240) surface, oklch(22% 0.02 240) text, oklch(72% 0.06 245) single accent reserved for active state only.

## Motion
Motion is absent by default. Only state transitions animate — 180ms opacity on focus, 240ms translate-y on new-content arrival. No ambient motion, no parallax, no shimmer.
Reduced-motion users see zero change; the design is already still.

## Notes
Do NOT generate: dashboard grids, card arrays, hero sections with gradient blobs, dark-mode-by-default, notification badges, floating action buttons, animated backgrounds, Figma-template sidebars with icon stacks. This Pathosformel refuses the maximalist SaaS surface — emptiness is the feature.
