# Reveal.js version

This directory contains a Reveal.js/HTML edition of `Quantum_Strategic_Infrastructure.pptx`.

The original PPTX is image-based: each slide is a full-slide PNG with no editable text objects. This HTML version preserves that visual fidelity by using the original slide images as backgrounds while making the deck structure, metadata, titles, and speaker notes editable in `index.html`.

## Open locally

From this directory:

```bash
python3 -m http.server 8088
```

Then open:

```text
http://localhost:8088
```

The current version loads Reveal.js from a CDN. If an offline version is needed, vendor the Reveal.js assets locally and update the paths in `index.html`.

## Edit

- Slide order and notes are in `index.html`.
- Cleaned visual slide images are in `assets/slides_clean/`; the original extracted images are preserved in `assets/slides/`.
- The Hadox Research Labs SVG mark is stored in `assets/brand/` and applied as an HTML/CSS overlay, so it can be changed without regenerating slide images.
- Presentation styling is in `theme.css`.
- Reveal.js configuration is in `deck.js`.

This is the low-risk first conversion: it preserves the original deck without destroying composition. A second pass can replace selected image text with editable HTML overlays.
