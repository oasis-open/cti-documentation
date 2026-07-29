# STIX documentation icons

These SVGs are derived from the
[STIX 2.1 Community SVG Icons](https://github.com/Kevinwochan/stix-2.1-community-svg-icons)
at commit `14fd9b4f24df5adafbf5392e73a4a51f4214abc5` and are provided under
this repository's BSD-3-Clause license. Each
label-free compatibility SVG declares the same 77-by-77 intrinsic dimensions
as its PNG predecessor. The historical PNG files are retained for
compatibility.

The icons are non-normative illustrations. Their shapes and ordinary object
colors do not add meaning to the STIX specification.

Two presentation forms are included:

- The flat files in this directory are transparent, label-free glyphs. Use
  them when nearby text already names the object, such as the object tables
  and walkthrough headings.
- `labeled/<category>/<slug>.svg` files are filled tiles with the readable
  object or marking name beneath the glyph. Use them when the artwork is the
  only visible type identifier, such as the example type cells, relationship
  selector, and nodes embedded in relationship diagrams.

The labeled path mirrors the source repository's
`icons/labeled/<category>/<slug>.svg` convention. Labels are font-free path
outlines, so their rendering does not depend on locally installed fonts.
They are part of the artwork for visual identification; surrounding Markdown
still supplies meaningful alternative text for assistive technology.

The TLP icons use the applicable FIRST display color as a filled STIX marking
tag, paired with an original path-drawn scope pictogram. These pictograms are
non-normative community artwork: the applicable FIRST color and literal
uppercase TLP label remain authoritative. Nearby native text must retain that
complete label and expose an accessible name, so neither color nor the
illustrative cue carries the meaning alone.

Render labeled TLP tiles at 96 CSS pixels or larger. At compact sizes, use the
label-free glyph with adjacent native text; path-drawn labels are visual
artwork and do not replace accessible application text. STIX 2.1 uses
TLP:WHITE, while TLP 2.0 uses TLP:CLEAR and also defines TLP:AMBER+STRICT;
applications should not silently reinterpret one vocabulary as the other.
