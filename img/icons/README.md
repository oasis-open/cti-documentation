# STIX documentation icons

These SVGs are derived from the
[STIX 2.1 Community SVG Icons](https://github.com/Kevinwochan/stix-2.1-community-svg-icons)
at commit `74dcd7bb0fd61e6418bd2f94b901e69955d3eb56` and are provided under
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
tag, paired with a path-drawn scope pictogram. Nearby text and labeled tiles
retain the complete uppercase marking name, so color is not the only cue.
STIX 2.1 uses TLP:WHITE, while TLP 2.0 uses TLP:CLEAR and also defines
TLP:AMBER+STRICT; applications should not silently reinterpret one vocabulary
as the other.
