#!/usr/bin/env python3
from __future__ import annotations

import csv
import html
import math
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGS = ROOT / "figures"

INK = "#1f2933"
MUTED = "#64748b"
GRID = "#d8dee9"
BLUE = "#2f6f9f"
TEAL = "#2a9d8f"
GOLD = "#b8871b"
RED = "#b4534a"
PURPLE = "#6d5bd0"
LIGHT = "#f6f8fb"


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def read_counts(path: Path) -> list[dict[str, object]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write_svg(path: Path, width: int, height: int, body: str) -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="white"/>
  <style>
    text {{ font-family: Arial, Helvetica, sans-serif; fill: {INK}; }}
    .title {{ font-size: 24px; font-weight: 700; }}
    .subtitle {{ font-size: 14px; fill: {MUTED}; }}
    .axis {{ font-size: 12px; fill: {MUTED}; }}
    .label {{ font-size: 13px; }}
    .small {{ font-size: 11px; fill: {MUTED}; }}
    .caption {{ font-size: 12px; fill: {MUTED}; }}
  </style>
{body}
</svg>
"""
    path.write_text(svg, encoding="utf-8")


def text(x: float, y: float, value: object, cls: str = "label", anchor: str = "start", weight: str | None = None) -> str:
    style = f' font-weight="{weight}"' if weight else ""
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}"{style}>{esc(value)}</text>'


def line(x1: float, y1: float, x2: float, y2: float, stroke: str = GRID, width: float = 1.0) -> str:
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{width}"/>'


def rect(x: float, y: float, w: float, h: float, fill: str, stroke: str = "none", rx: float = 0) -> str:
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" stroke="{stroke}" rx="{rx}"/>'


def path(points: list[tuple[float, float]], stroke: str, width: float = 3) -> str:
    d = " ".join(("M" if i == 0 else "L") + f"{x:.1f},{y:.1f}" for i, (x, y) in enumerate(points))
    return f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{width}" stroke-linejoin="round" stroke-linecap="round"/>'


def figure_country_distribution() -> None:
    rows = read_counts(DATA / "openalex_quantum_technology_country_counts_2015_2025.csv")
    top = rows[:10]
    mexico = next(r for r in rows if r["country_code"] == "MX")
    chart = top + [mexico]
    short = {
        "United States of America": "United States",
        "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
        "Korea, Republic of": "Korea",
    }
    width, height = 1200, 760
    x0, y0, plot_w = 270, 120, 780
    bar_h, gap = 34, 16
    max_count = max(int(r["count"]) for r in chart)
    body = []
    body.append(text(52, 48, "Global distribution of quantum-technology publications", "title"))
    body.append(text(52, 74, "OpenAlex concept C190463098, country-affiliation counts, 2015-2025; Mexico shown for comparison.", "subtitle"))
    for tick in range(0, max_count + 1, 500):
        x = x0 + plot_w * tick / max_count
        body.append(line(x, y0 - 20, x, y0 + len(chart) * (bar_h + gap) - gap + 10, GRID, 0.8))
        body.append(text(x, y0 - 30, f"{tick:,}", "axis", "middle"))
    for i, row in enumerate(chart):
        y = y0 + i * (bar_h + gap)
        count = int(row["count"])
        country = short.get(row["country"], row["country"])
        fill = RED if row["country_code"] == "MX" else BLUE
        if row["country_code"] == "MX":
            body.append(line(x0 - 15, y - 8, x0 + plot_w, y - 8, "#9aa6b2", 1.2))
        body.append(text(x0 - 18, y + 23, country, "label", "end"))
        body.append(rect(x0, y, plot_w * count / max_count, bar_h, fill, rx=3))
        body.append(text(x0 + plot_w * count / max_count + 10, y + 23, f"{count:,}", "label"))
    body.append(text(52, 716, "Source: OpenAlex Works API extraction. Counts are bibliometric adoption proxies, not direct deployment measures.", "caption"))
    write_svg(FIGS / "fig1_global_country_distribution.svg", width, height, "\n".join(body))


def figure_publication_trends() -> None:
    qt = [(int(r["year"]), int(r["count"])) for r in read_counts(DATA / "openalex_quantum_technology_year_counts_2015_2025.csv")]
    pqc = [(int(r["year"]), int(r["count"])) for r in read_counts(DATA / "openalex_post_quantum_crypto_year_counts_2015_2025.csv")]
    qt_idx = [(y, c / qt[0][1] * 100) for y, c in qt]
    pqc_idx = [(y, c / pqc[0][1] * 100) for y, c in pqc]
    all_vals = [v for _, v in qt_idx + pqc_idx]
    max_val = math.ceil(max(all_vals) / 200) * 200
    width, height = 1200, 720
    x0, y0, plot_w, plot_h = 95, 115, 980, 470
    years = [y for y, _ in qt]

    def sx(year: int) -> float:
        return x0 + (year - years[0]) / (years[-1] - years[0]) * plot_w

    def sy(value: float) -> float:
        return y0 + plot_h - value / max_val * plot_h

    body = []
    body.append(text(52, 48, "Publication trajectory of quantum-technology and PQC literatures", "title"))
    body.append(text(52, 74, "Indexed OpenAlex year counts, 2015=100. The index enables comparison across differently sized literatures.", "subtitle"))
    for tick in range(0, max_val + 1, 200):
        y = sy(tick)
        body.append(line(x0, y, x0 + plot_w, y, GRID, 0.8))
        body.append(text(x0 - 12, y + 4, tick, "axis", "end"))
    for year in years:
        x = sx(year)
        body.append(line(x, y0 + plot_h, x, y0 + plot_h + 6, MUTED, 1))
        body.append(text(x, y0 + plot_h + 25, year, "axis", "middle"))
    body.append(line(x0, y0, x0, y0 + plot_h, MUTED, 1.2))
    body.append(line(x0, y0 + plot_h, x0 + plot_w, y0 + plot_h, MUTED, 1.2))
    body.append(path([(sx(y), sy(v)) for y, v in qt_idx], BLUE, 3.2))
    body.append(path([(sx(y), sy(v)) for y, v in pqc_idx], TEAL, 3.2))
    for y, v in qt_idx:
        body.append(f'<circle cx="{sx(y):.1f}" cy="{sy(v):.1f}" r="4.5" fill="{BLUE}"/>')
    for y, v in pqc_idx:
        body.append(f'<circle cx="{sx(y):.1f}" cy="{sy(v):.1f}" r="4.5" fill="{TEAL}"/>')
    body.append(rect(790, 112, 18, 18, BLUE, rx=2))
    body.append(text(818, 127, "Quantum technology", "label"))
    body.append(rect(790, 142, 18, 18, TEAL, rx=2))
    body.append(text(818, 157, "Post-quantum cryptography", "label"))
    body.append(text(50, 350, "Index, 2015=100", "axis"))
    body.append(text(52, 682, "Source: OpenAlex Works API extraction. The 2025 quantum-technology spike is interpreted as an indexing/query signal requiring cautious interpretation.", "caption"))
    write_svg(FIGS / "fig2_publication_trends.svg", width, height, "\n".join(body))


def figure_readiness_gap() -> None:
    rows = [
        ("UK executives", 97, "expect disruption", 33, "readiness planning"),
        ("Financial services", 87, "see opportunity", 27, "identified use case"),
        ("Financial services", 87, "see opportunity", 13, "dedicated budget"),
        ("Digital trust/risk", 64, "expect impact", 20, "formal readiness plan"),
    ]
    width, height = 1200, 720
    x0, y0, plot_w = 250, 135, 820
    group_h = 110
    body = []
    body.append(text(52, 48, "Awareness-readiness gap in quantum computing adoption", "title"))
    body.append(text(52, 74, "Survey evidence summarized by OECD shows high expected impact but substantially lower planning and budget readiness.", "subtitle"))
    for tick in range(0, 101, 20):
        x = x0 + plot_w * tick / 100
        body.append(line(x, y0 - 20, x, y0 + len(rows) * group_h - 22, GRID, 0.8))
        body.append(text(x, y0 - 30, f"{tick}%", "axis", "middle"))
    for i, (sample, high, high_label, low, low_label) in enumerate(rows):
        y = y0 + i * group_h
        body.append(text(x0 - 20, y + 28, sample, "label", "end", "700"))
        body.append(rect(x0, y, plot_w * high / 100, 26, BLUE, rx=3))
        body.append(text(x0 + plot_w * high / 100 + 9, y + 19, f"{high}% {high_label}", "label"))
        body.append(rect(x0, y + 42, plot_w * low / 100, 26, GOLD, rx=3))
        body.append(text(x0 + plot_w * low / 100 + 9, y + 61, f"{low}% {low_label}", "label"))
    body.append(rect(780, 618, 18, 18, BLUE, rx=2))
    body.append(text(808, 633, "Expectation or perceived opportunity", "label"))
    body.append(rect(780, 648, 18, 18, GOLD, rx=2))
    body.append(text(808, 663, "Planning, use-case, or budget readiness", "label"))
    body.append(text(52, 682, "Source: OECD business-readiness synthesis of EY/NQCC, Moody's, and ISACA survey evidence.", "caption"))
    write_svg(FIGS / "fig3_readiness_gap.svg", width, height, "\n".join(body))


def heat_color(score: int) -> str:
    colors = {0: "#f1f5f9", 1: "#cfe7ef", 2: "#73b6c8", 3: "#2f6f9f"}
    return colors[score]


def figure_capability_heatmap() -> None:
    domains = ["PQC", "Sensing", "QCaaS", "Communication", "Standards", "Workforce", "Frontier R&D"]
    phases = ["2025-2027\nPreparation", "2027-2030\nTestbeds", "2030-2035\nScaling"]
    scores = [
        [3, 3, 3],
        [2, 3, 3],
        [2, 3, 2],
        [1, 2, 3],
        [2, 3, 3],
        [3, 3, 3],
        [2, 2, 3],
    ]
    width, height = 1200, 740
    x0, y0, cell_w, cell_h = 295, 150, 245, 72
    body = []
    body.append(text(52, 48, "Sequencing of national quantum capabilities", "title"))
    body.append(text(52, 74, "Darker cells indicate higher strategic priority in each phase of a 2025-2035 national roadmap.", "subtitle"))
    for j, phase in enumerate(phases):
        x = x0 + j * cell_w + cell_w / 2
        p1, p2 = phase.split("\n")
        body.append(text(x, y0 - 40, p1, "label", "middle", "700"))
        body.append(text(x, y0 - 20, p2, "small", "middle"))
    for i, domain in enumerate(domains):
        y = y0 + i * cell_h
        body.append(text(x0 - 24, y + 44, domain, "label", "end", "700"))
        for j, score in enumerate(scores[i]):
            x = x0 + j * cell_w
            body.append(rect(x, y, cell_w - 8, cell_h - 8, heat_color(score), "#ffffff", rx=4))
            body.append(text(x + cell_w / 2 - 4, y + 41, score, "label", "middle", "700"))
    legend_x, legend_y = 292, 690
    for score, label in [(0, "not central"), (1, "watch"), (2, "build"), (3, "priority")]:
        body.append(rect(legend_x + score * 160, legend_y, 34, 18, heat_color(score), "#ffffff", rx=2))
        body.append(text(legend_x + score * 160 + 42, legend_y + 14, label, "small"))
    body.append(text(52, 682, "Source: Author synthesis from adoption literature, OECD readiness evidence, NIST PQC standards, and OpenAlex bibliometrics.", "caption"))
    write_svg(FIGS / "fig4_capability_heatmap.svg", width, height, "\n".join(body))


def figure_roadmap_timeline() -> None:
    width, height = 1200, 620
    x0, y = 120, 190
    total_w = 960
    phases = [
        ("2025-2027", "Preparation and security", "PQC inventories\nQCaaS access\nWorkforce curricula\nSensing feasibility"),
        ("2027-2030", "Testbeds and pilots", "Sensing pilots\nPQC staged migration\nBenchmark lab\nQKD where justified"),
        ("2030-2035", "Selective scaling", "Operational sensing\nQuantum networks\nLogical-qubit readiness\nFrontier research"),
    ]
    widths = [250, 310, 400]
    colors = [BLUE, TEAL, PURPLE]
    body = []
    body.append(text(52, 48, "National quantum roadmap, 2025-2035", "title"))
    body.append(text(52, 74, "Capability accumulation proceeds through preparation, operational learning, and selective scaling.", "subtitle"))
    x = x0
    for i, (period, title, details) in enumerate(phases):
        w = widths[i]
        body.append(rect(x, y, w, 90, colors[i], rx=8))
        body.append(text(x + 18, y + 30, period, "label", "start", "700"))
        body.append(text(x + 18, y + 58, title, "label", "start", "700"))
        if i < len(phases) - 1:
            body.append(f'<polygon points="{x+w},{y+15} {x+w+45},{y+45} {x+w},{y+75}" fill="{colors[i]}"/>')
        detail_y = y + 135
        for k, item in enumerate(details.split("\n")):
            body.append(rect(x + 4, detail_y + k * 34 - 17, 10, 10, colors[i], rx=5))
            body.append(text(x + 24, detail_y + k * 34 - 8, item, "label"))
        x += w + 55
    body.append(line(x0, y + 112, x0 + total_w, y + 112, "#9aa6b2", 1.3))
    for year, xpos in [(2025, x0), (2027, x0 + widths[0]), (2030, x0 + widths[0] + 55 + widths[1]), (2035, x0 + total_w)]:
        body.append(line(xpos, y + 104, xpos, y + 122, MUTED, 1.2))
        body.append(text(xpos, y + 146, year, "axis", "middle"))
    body.append(text(52, 584, "Source: Author synthesis. Roadmap phases are capability milestones rather than hardware-breakthrough predictions.", "caption"))
    write_svg(FIGS / "fig5_roadmap_timeline.svg", width, height, "\n".join(body))


def figure_mexico_institutions() -> None:
    rows = [
        ("UNAM", 20),
        ("IPN", 13),
        ("Tecnologico de Monterrey", 10),
        ("Other Mexico-affiliated works", 13),
    ]
    width, height = 1100, 610
    x0, y0, plot_w = 290, 120, 690
    max_count = 20
    body = []
    body.append(text(52, 48, "Mexico-affiliated quantum-technology research base", "title"))
    body.append(text(52, 74, "OpenAlex concept C190463098, institution counts in the 2015-2025 Mexico-affiliated subset.", "subtitle"))
    for tick in range(0, max_count + 1, 5):
        x = x0 + plot_w * tick / max_count
        body.append(line(x, y0 - 20, x, y0 + 275, GRID, 0.8))
        body.append(text(x, y0 - 30, tick, "axis", "middle"))
    for i, (name, count) in enumerate(rows):
        y = y0 + i * 72
        fill = RED if name == "Other Mexico-affiliated works" else BLUE
        body.append(text(x0 - 18, y + 28, name, "label", "end", "700" if i < 3 else None))
        body.append(rect(x0, y, plot_w * count / max_count, 34, fill, rx=3))
        body.append(text(x0 + plot_w * count / max_count + 10, y + 24, count, "label"))
    body.append(text(52, 560, "Source: OpenAlex Works API extraction. Institution counts are bibliometric proxies and do not measure deployment or industrial readiness.", "caption"))
    write_svg(FIGS / "fig6_mexico_institutions.svg", width, height, "\n".join(body))


def figure_mexico_domain_priority() -> None:
    domains = ["PQC", "Sensing", "QCaaS", "Communication", "Frontier R&D"]
    criteria = ["Urgency", "Feasibility", "Public value", "Sovereignty"]
    scores = [
        [3, 3, 3, 3],
        [2, 2, 3, 2],
        [2, 3, 2, 2],
        [1, 1, 2, 2],
        [2, 1, 2, 3],
    ]
    width, height = 1150, 650
    x0, y0, cell_w, cell_h = 280, 135, 190, 70
    body = []
    body.append(text(52, 48, "Domain priorities for Mexican quantum readiness", "title"))
    body.append(text(52, 74, "Scored synthesis: 0=not central, 1=monitor, 2=build, 3=priority for 2025-2035 capability formation.", "subtitle"))
    for j, criterion in enumerate(criteria):
        body.append(text(x0 + j * cell_w + cell_w / 2, y0 - 26, criterion, "label", "middle", "700"))
    for i, domain in enumerate(domains):
        y = y0 + i * cell_h
        body.append(text(x0 - 24, y + 42, domain, "label", "end", "700"))
        for j, score in enumerate(scores[i]):
            x = x0 + j * cell_w
            body.append(rect(x, y, cell_w - 8, cell_h - 8, heat_color(score), "#ffffff", rx=4))
            body.append(text(x + cell_w / 2 - 4, y + 40, score, "label", "middle", "700"))
    body.append(text(52, 600, "Source: Author synthesis from OECD readiness data, NIST PQC standards, OpenAlex Mexico counts, and domain-readiness literature.", "caption"))
    write_svg(FIGS / "fig7_mexico_domain_priority.svg", width, height, "\n".join(body))


def convert_svgs() -> None:
    for svg in FIGS.glob("fig*.svg"):
        png = svg.with_suffix(".png")
        subprocess.run(["rsvg-convert", "-w", "1800", str(svg), "-o", str(png)], check=True)


def main() -> None:
    FIGS.mkdir(exist_ok=True)
    figure_country_distribution()
    figure_publication_trends()
    figure_readiness_gap()
    figure_capability_heatmap()
    figure_roadmap_timeline()
    figure_mexico_institutions()
    figure_mexico_domain_priority()
    convert_svgs()


if __name__ == "__main__":
    main()
