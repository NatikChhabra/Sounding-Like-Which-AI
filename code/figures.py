"""Paper figures (PDF) from results/*. Usage: python figures.py
Palette: reference categorical slots 1-3 (validated all-pairs for CVD); text in ink, never series color.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

RES = Path(__file__).resolve().parent.parent / "results"
FIG = Path(__file__).resolve().parent.parent / "paper" / "figures"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
T0 = pd.Period("2022-12", "M")

plt.rcParams.update({"font.family": "serif", "font.size": 8, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.5,
                     "legend.frameon": False, "pdf.fonttype": 42})


def its_panel(ax, name, color, label, ylabel="MSO (%)", legend=False):
    m = pd.read_csv(RES / f"{name}.csv")
    m["month"] = pd.PeriodIndex(m.month, freq="M")
    t = np.array([(p - T0).n for p in m.month])
    x = m.month.dt.to_timestamp()
    ax.scatter(x, 100 * m.mso, s=6, color=color, alpha=0.45, linewidths=0, label="monthly value")
    pre = t < 0
    b = np.polyfit(t[pre], 100 * m.mso[pre], 1, w=np.sqrt(m.n[pre]))
    ax.plot(x, np.polyval(b, t), color=MUTED, lw=1, ls="--", label="pre-ChatGPT trend, extrapolated")
    roll = (100 * m.mso).rolling(6, center=True, min_periods=3).mean()
    ax.plot(x, roll, color=color, lw=2, label="centred 6-month mean")
    ax.axvline(T0.to_timestamp(), color=INK, lw=0.6)
    ax.text(T0.to_timestamp(), ax.get_ylim()[0], " ChatGPT", color=INK, va="bottom", fontsize=6.5)
    ax.set_ylabel(ylabel)
    if legend:
        ax.legend(loc="upper left", fontsize=6)


def fig_timeseries():
    fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.3), sharex=True)
    its_panel(axes[0], "arxiv_monthly", BLUE, "arXiv", legend=True)
    axes[0].set_title("(a) MSO, arXiv abstracts", fontsize=8, color=INK, loc="left")
    its_panel(axes[1], "hansard_monthly", ORANGE, "Hansard")
    axes[1].set_title("(b) MSO, parliamentary speech", fontsize=8, color=INK, loc="left")
    its_panel(axes[2], "arxiv_marker_monthly", AQUA, "arXiv", ylabel="Abstracts with marker word (%)")
    axes[2].set_title("(c) Marker words, arXiv", fontsize=8, color=INK, loc="left")
    for ax in axes:
        ax.tick_params(axis="x", labelsize=6.5)
        ax.xaxis.set_major_locator(matplotlib.dates.YearLocator(3))
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
    fig.tight_layout()
    fig.savefig(FIG / "timeseries.pdf")


def fig_fields():
    base = pd.read_csv(RES / "arxiv_baseline_pre2022.csv")
    its = json.loads((RES / "arxiv_its.json").read_text())
    base = base[base.group.isin([g for g in its if g in base.group.values and g != "all"])].sort_values("mso")
    ex = [its[g] for g in base.group]
    k = "excess"
    fig, axes = plt.subplots(1, 2, figsize=(3.3, 2.1), sharey=True, gridspec_kw={"wspace": 0.08})
    y = np.arange(len(base))
    axes[0].errorbar(100 * base.mso, y, xerr=[100 * (base.mso - base.lo), 100 * (base.hi - base.mso)],
                     fmt="o", ms=4, color=BLUE, ecolor=BLUE, elinewidth=1, capsize=0)
    axes[0].set_yticks(y, base.group)
    axes[0].set_xlabel("Pre-ChatGPT MSO (%)", fontsize=7)
    e = np.array([100 * d[k] for d in ex])
    lo = np.array([100 * d["excess_lo"] for d in ex])
    hi = np.array([100 * d["excess_hi"] for d in ex])
    axes[1].errorbar(e, y, xerr=[e - lo, hi - e], fmt="o", ms=4, color=BLUE, ecolor=BLUE, elinewidth=1, capsize=0)
    axes[1].axvline(0, color=MUTED, lw=0.6)
    axes[1].set_xlabel("Trend gap, June 2025 (pp)", fontsize=7)
    for ax in axes:
        ax.tick_params(labelsize=6.5)
    fig.subplots_adjust(left=0.2, right=0.98, bottom=0.2, top=0.97)
    fig.savefig(FIG / "fields.pdf")


def fig_learners():
    inst = [("Style features\n(primary)", "essay_mso_by_group"), ("Sentence\nembeddings", "essay_embedding_instrument"),
            ("Perplexity\n(detector-style)", "essay_perplexity_instrument")]
    inst = [(n, pd.read_csv(RES / f"{f}.csv").set_index("group")) for n, f in inst if (RES / f"{f}.csv").exists()]
    fig, ax = plt.subplots(figsize=(3.1, 0.6 + 0.55 * len(inst)))
    for i, (name, df) in enumerate(inst[::-1]):
        for j, (g, c) in enumerate([("non-ELL", BLUE), ("ELL", ORANGE)]):
            r = df.loc[g]
            yy = i + (0.15 if j == 0 else -0.15)
            ax.errorbar(100 * r.mso, yy, xerr=[[100 * (r.mso - r.lo)], [100 * (r.hi - r.mso)]], fmt="o", ms=4,
                        color=c, ecolor=c, elinewidth=1, capsize=0, label=g if i == 0 else None)
    ax.set_yticks(range(len(inst)), [n for n, _ in inst[::-1]], fontsize=6.5)
    ax.set_xlabel("Share of held-out essays flagged as LLM-like (%)", fontsize=7)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.32), ncol=2, fontsize=6.5)
    fig.tight_layout()
    fig.savefig(FIG / "learners.pdf")


def fig_gensets():
    g = pd.read_csv(RES / "arxiv_gensets.csv").set_index("group")
    years = [int(c[1:]) for c in g.columns if c.startswith("y")]
    sets = [("all", "All 14 generators", BLUE), ("local_frontier", "Local 7 + 2026 model", ORANGE),
            ("local", "Local 7 (2024-25 open models)", AQUA), ("no_frontier", "All except 2026 model", "#eda100"),
            ("raid", "RAID only (2023 models)", "#e87ba4")]
    fig, ax = plt.subplots(figsize=(3.3, 2.3))
    for k, label, c in sets:
        y = [100 * g.loc[k, f"y{yr}"] for yr in years]
        ax.plot(years, y, color=c, lw=2, marker="o", ms=3, label=label)
    ax.axvline(2022.9, color=INK, lw=0.6)
    ax.set_ylabel("arXiv MSO (%)")
    ax.set_xticks([2015, 2018, 2021, 2024, 2026])
    ax.legend(fontsize=5.8, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIG / "gensets.pdf")


if __name__ == "__main__":
    FIG.mkdir(parents=True, exist_ok=True)
    for f in (fig_learners, fig_timeseries, fig_fields, fig_gensets):
        try:
            f()
            print("ok", f.__name__)
        except FileNotFoundError as e:
            print("skip", f.__name__, "(missing", Path(e.filename).name + ")")
