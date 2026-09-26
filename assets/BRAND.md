# Publicist Skills identity

Publicist Skills uses an editorial identity based on bright newsprint, dark broadsheet ink, and a measured quotation-mark lockup. The system should feel precise and established without imitating a specific newspaper.

## Core colors

| Name | Hex | Use |
|---|---|---|
| Newsprint | `#F7F3EA` | Primary background |
| Broadsheet navy | `#102235` | Wordmark, quotation mark, subtitle, and primary text |

Use the two colors without gradients, shadows, transparency effects, or decorative outlines.

## Logo lockup

The lockup uses the Publicist wordmark in Grenze Regular and the native opening quotation glyph from Grenze Light. Its spacing is measured from the visible wordmark height, `H`:

- quotation-mark height: `1.00H`;
- optical gap between the mark and wordmark: `0.40H`;
- alignment: the visible top and bottom bounds of both elements share the same horizontal guides.

Keep these proportions when resizing the lockup. Do not stretch, rotate, recolor, rearrange, or redraw either element.

## Repository hero

The final repository hero is `1600 × 900` pixels. The complete title-and-subtitle group is centered vertically, with 308 pixels of clear space above and below, and includes this exact line:

> Skills for media research and pitch strategy across five markets

The line has no final period. It is set in Alegreya Regular, centered below the lockup, in broadsheet navy. Do not add another subtitle, badge, rule, texture, or decorative element inside the hero.

[`repository-hero.png`](repository-hero.png) is the GitHub hero image. [`repository-hero.svg`](repository-hero.svg) wraps that raster image; it is not an editable vector master.

## Asset files

- [`logo-mark.svg`](logo-mark.svg) contains the quotation-mark icon on newsprint.
- [`wordmark.svg`](wordmark.svg) contains the Publicist wordmark.
- [`logo-lockup.svg`](logo-lockup.svg) combines the measured quotation mark and wordmark.
- [`repository-hero.svg`](repository-hero.svg) is a 1600 × 900 wrapper for the PNG hero.
- [`repository-hero.png`](repository-hero.png) is the English README hero.
- Localized README heroes retain the PUBLICIST wordmark and translate the subline: [German](repository-hero.de.png), [Simplified Chinese](repository-hero.zh-CN.png), [Japanese](repository-hero.ja.png), and [Brazilian Portuguese](repository-hero.pt-BR.png). Each is a 1600 × 900 PNG.

The logo and wordmark SVGs store type as glyph outlines and need no local or remote fonts at render time. The hero SVG embeds the PNG. The repository does not distribute a font binary. Grenze and Alegreya are released under the SIL Open Font License.
