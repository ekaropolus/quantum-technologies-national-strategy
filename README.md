# Quantum Technologies National Strategy Research Compendium

Research compendium for quantum technologies, national capability formation, post-quantum readiness, and Mexican digital transformation.

This repository contains papers, presentation material, data, figures, bibliography, and reproducible build scripts prepared for the Quantum Technologies track of the twenty-third edition of the Global Information Technology Management Association Annual Conference, Monterrey, Mexico, May 6-8, 2026.

Edgar Antonio Valdes Porras served as Track Chair for the Quantum Technologies track.

## Start Here

If you are looking for the research papers, use the links below. Each paper is available as PDF for reading and Markdown/Tex/DOCX for inspection or reuse.

## Papers And Research Outputs

| Output | Language | PDF | Source | Other formats |
| --- | --- | --- | --- | --- |
| Quantum Technologies as Strategic Infrastructure: Evidence, Adoption Pathways, and a National Research Agenda for 2025-2035 | English | [PDF](quantum_technologies_research_paper.pdf) | [Markdown](quantum_technologies_research_paper.md) | [TeX](quantum_technologies_research_paper.tex), [DOCX](quantum_technologies_research_paper.docx) |
| A National Roadmap for Quantum Technologies: Strategic Infrastructure, Sovereign Capability, and Research Priorities for 2025-2035 | English | [PDF](national_quantum_technology_roadmap_2025_2035.pdf) | [Markdown](national_quantum_technology_roadmap_2025_2035.md) | [TeX](national_quantum_technology_roadmap_2025_2035.tex), [DOCX](national_quantum_technology_roadmap_2025_2035.docx) |
| Perspectives on Quantum Technologies in Mexican Digital Transformation | English | [PDF](quantum_technologies_mexican_digital_transformation.pdf) | [Markdown](quantum_technologies_mexican_digital_transformation.md) | [TeX](quantum_technologies_mexican_digital_transformation.tex), [DOCX](quantum_technologies_mexican_digital_transformation.docx) |
| Tecnologias cuanticas como infraestructura estrategica: evidencia, rutas de adopcion y una agenda nacional de investigacion para 2025-2035 | Spanish | [PDF](tecnologias_cuanticas_infraestructura_estrategica.pdf) | [Markdown](tecnologias_cuanticas_infraestructura_estrategica.md) | [TeX](tecnologias_cuanticas_infraestructura_estrategica.tex), [DOCX](tecnologias_cuanticas_infraestructura_estrategica.docx) |
| Guia nacional de tecnologias cuanticas 2025-2035 | Spanish | [PDF](guia_nacional_tecnologias_cuanticas_2025_2035.pdf) | [Markdown](guia_nacional_tecnologias_cuanticas_2025_2035.md) | [TeX](guia_nacional_tecnologias_cuanticas_2025_2035.tex), [DOCX](guia_nacional_tecnologias_cuanticas_2025_2035.docx) |
| Perspectivas sobre tecnologias cuanticas en la transformacion digital mexicana | Spanish | [PDF](perspectivas_tecnologias_cuanticas_transformacion_digital_mexicana.pdf) | [Markdown](perspectivas_tecnologias_cuanticas_transformacion_digital_mexicana.md) | [TeX](perspectivas_tecnologias_cuanticas_transformacion_digital_mexicana.tex), [DOCX](perspectivas_tecnologias_cuanticas_transformacion_digital_mexicana.docx) |

## Presentation

- [Live Reveal.js presentation](https://hadox-research-labs.github.io/quantum-technologies-national-strategy/)
- [Presentation PDF](Quantum_Strategic_Infrastructure_presentation.pdf)
- [Reveal.js source directory](reveal_quantum_strategic_infrastructure/)
- [Paper-to-slide map](reveal_quantum_strategic_infrastructure/paper_slide_map.md)
- [Speaker script](reveal_quantum_strategic_infrastructure/speaker_script.md)

The presentation is a companion output. The papers above are the primary research artifacts.

## Repository Map

| Path | Purpose |
| --- | --- |
| `data/` | Processed OpenAlex CSV extracts used as descriptive evidence. |
| `figures/` | SVG and PNG figures used in the papers. |
| `quantum_references.bib` | Shared BibTeX bibliography used by Pandoc citeproc. |
| `scripts/build_quantum_papers.sh` | Rebuilds PDF, TeX, and DOCX outputs from Markdown sources. |
| `scripts/generate_quantum_figures.py` | Regenerates the figures from processed data. |
| `CODE_AVAILABILITY.md` | Reproducibility and code-availability statement. |
| `CITATION.cff` | Repository-level citation metadata. |
| `COMMAND_CENTER.md` | Local command-center placement notes for the author's workstation. |

## Reproducibility

The papers are built with Pandoc citeproc and XeLaTeX:

```bash
PANDOC=/path/to/pandoc ./scripts/build_quantum_papers.sh
```

Pandoc 3.x is recommended because citeproc is built in. The build script uses the local Pandoc 3 binary on the author's workstation when present, otherwise it falls back to `pandoc` on `PATH`.

Figure regeneration requires Python 3 and `rsvg-convert`:

```bash
python3 scripts/generate_quantum_figures.py
```

## Data

The processed CSV files in `data/` are descriptive extracts from the public OpenAlex API. They are used as bibliometric proxies for scientific absorptive capacity and are not interpreted as direct deployment or adoption metrics.

Other quantitative indicators used in the papers are cited to public OECD, OECD-EPO, NIST, NSA, CISA, and related sources in `quantum_references.bib`.

## Citation

Please cite the specific manuscript used. Repository-level citation metadata are provided in [CITATION.cff](CITATION.cff).

## License

Manuscripts, figures, and processed data are released under CC BY 4.0 unless otherwise noted. Code in `scripts/` is released under the MIT License. See [LICENSE.md](LICENSE.md).
