#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ -z "${PANDOC:-}" ]]; then
  if [[ -x /home/hadox/.local/pandoc3/pandoc-3.1.13/bin/pandoc ]]; then
    PANDOC=/home/hadox/.local/pandoc3/pandoc-3.1.13/bin/pandoc
  else
    PANDOC=pandoc
  fi
fi

papers=(
  quantum_technologies_research_paper
  national_quantum_technology_roadmap_2025_2035
  quantum_technologies_mexican_digital_transformation
)

for paper in "${papers[@]}"; do
  "$PANDOC" "$ROOT/$paper.md" --resource-path="$ROOT:." -s --citeproc --shift-heading-level-by=-1 \
    -V documentclass=article -V fontsize=11pt -V geometry:margin=1in \
    -V colorlinks=true -V linkcolor=blue -V citecolor=blue -V urlcolor=blue -V filecolor=blue \
    -V papersize=letter -V secnumdepth=0 \
    -o "$ROOT/$paper.tex"

  "$PANDOC" "$ROOT/$paper.md" --resource-path="$ROOT:." -s --citeproc --shift-heading-level-by=-1 \
    --pdf-engine=xelatex \
    -V documentclass=article -V fontsize=11pt -V geometry:margin=1in \
    -V colorlinks=true -V linkcolor=blue -V citecolor=blue -V urlcolor=blue -V filecolor=blue \
    -V papersize=letter -V secnumdepth=0 \
    -o "$ROOT/$paper.pdf"

  "$PANDOC" "$ROOT/$paper.md" --resource-path="$ROOT:." -s --citeproc --shift-heading-level-by=-1 \
    -o "$ROOT/$paper.docx"
done

for ext in md tex pdf docx; do
  cp "$ROOT/national_quantum_technology_roadmap_2025_2035.$ext" "$ROOT/guia_nacional_tecnologias_cuanticas_2025_2035.$ext"
  cp "$ROOT/quantum_technologies_mexican_digital_transformation.$ext" "$ROOT/perspectivas_tecnologias_cuanticas_transformacion_digital_mexicana.$ext"
done
