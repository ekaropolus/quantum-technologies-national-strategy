# Quantum Technologies National Strategy Research Compendium

This repository is the companion research archive for three manuscripts on quantum technologies, national capability formation, and Mexican digital transformation:

- `quantum_technologies_research_paper.*`: broad research synthesis on quantum technologies as strategic infrastructure.
- `national_quantum_technology_roadmap_2025_2035.*`: national roadmap for quantum capability formation during 2025-2035.
- `quantum_technologies_mexican_digital_transformation.*`: Mexico-oriented paper on quantum technologies within digital transformation.

The manuscripts were prepared for the Quantum Technologies track of the twenty-third edition of the Global Information Technology Management Association Annual Conference, Monterrey, Mexico, May 6-8, 2026. Edgar Antonio Valdés Porras serves as Track Chair for the Quantum Technologies track.

## Repository Contents

- `*.md`: manuscript sources in Pandoc Markdown.
- `*.tex`: generated LaTeX files.
- `*.pdf`: compiled PDF versions.
- `*.docx`: generated Word versions.
- `quantum_references.bib`: shared BibTeX bibliography used by Pandoc citeproc.
- `data/`: processed OpenAlex CSV extracts used as descriptive evidence.
- `figures/`: SVG and PNG figures used in the papers.
- `scripts/generate_quantum_figures.py`: figure-generation script.
- `scripts/build_quantum_papers.sh`: reproducible build script for PDF, TeX, and DOCX outputs.

## Reproducibility

The papers are built with Pandoc citeproc and XeLaTeX. A typical build is:

```bash
PANDOC=/path/to/pandoc ./scripts/build_quantum_papers.sh
```

Pandoc 3.x is recommended because citeproc is built in. The build script uses the local Pandoc 3 binary on the author's workstation when present, otherwise it falls back to `pandoc` on `PATH`.

Figure regeneration requires Python 3 and `rsvg-convert`:

```bash
python3 scripts/generate_quantum_figures.py
```

## Data

The processed CSV files in `data/` are descriptive extracts from the public OpenAlex API. They are used as bibliometric proxies for scientific absorptive capacity and are not interpreted as direct deployment or adoption metrics. Other quantitative indicators used in the papers are cited to public OECD, OECD-EPO, NIST, NSA, CISA, and related sources in the bibliography.

## Citation

Please cite the specific manuscript used. Repository-level citation metadata are provided in `CITATION.cff`.

## License

Manuscripts, figures, and processed data are released under CC BY 4.0 unless otherwise noted. Code in `scripts/` is released under the MIT License. See `LICENSE.md`.
