"""Paper figures (PDF) from results/*. Usage: python figures.py
Palette: reference categorical slots 1-3 (validated all-pairs for CVD); text in ink, never series color.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
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


def its_panel(ax, name, color, label, ylabel="MSO (% of human docs in LLM region)"):
    m = pd.read_csv(RES / f"{name}.csv")
    m["month"] = pd.PeriodIndex(m.month, freq="M")
    t = np.array([(p - T0).n for p in m.month])
    x = m.month.dt.to_timestamp()
    ax.scatter(x, 100 * m.mso, s=6, color=color, alpha=0.45, linewidths=0, label=f"{label}, monthly")
    pre = t < 0
    b = np.polyfit(t[pre], 100 * m.mso[pre], 1, w=np.sqrt(m.n[pre]))
    ax.plot(x, np.polyval(b, t), color=MUTED, lw=1, ls="--", label="pre-2022 trend, extrapolated")
    roll = (100 * m.mso).rolling(6, center=True, min_periods=3).mean()
    ax.plot(x, roll, color=color, lw=2, label="6-month mean")
    ax.axvline(T0.to_timestamp(), color=INK, lw=0.6)
    ax.text(T0.to_timestamp(), ax.get_ylim()[1], " ChatGPT", color=INK, va="top", fontsize=7)
    ax.set_ylabel(ylabel)
    ax.legend(loc="upper left", fontsize=6)


def fig_timeseries():
    fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.3), sharex=True)
    its_panel(axes[0], "arxiv_monthly", BLUE, "arXiv")
    axes[0].set_title("(a) MSO, arXiv abstracts", fontsize=8, color=INK, loc="left")
    its_panel(axes[1], "hansard_monthly", ORANGE, "Hansard")
    axes[1].set_title("(b) MSO, parliamentary speech", fontsize=8, color=INK, loc="left")
    its_panel(axes[2], "arxiv_marker_monthly", AQUA, "arXiv", ylabel="% of abstracts with a marker word")
    axes[2].set_title("(c) Marker words, arXiv", fontsize=8, color=INK, loc="left")
    for ax in axes:
        ax.tick_params(axis="x", labelrotation=45, labelsize=6.5)
    fig.tight_layout()
    fig.savefig(FIG / "timeseries.pdf")


def fig_fields():
    base = pd.read_csv(RES / "arxiv_baseline_pre2022.csv")
    its = json.loads((RES / "arxiv_its.json").read_text())
    base = base[base.group != "all"].sort_values("mso")
    ex = [its[g] for g in base.group]
    k = next(k for k in ex[0] if k.startswith("excess_at"))
    fig, axes = plt.subplots(1, 2, figsize=(6.3, 2.2), sharey=True)
    y = np.arange(len(base))
    axes[0].errorbar(100 * base.mso, y, xerr=[100 * (base.mso - base.lo), 100 * (base.hi - base.mso)],
                     fmt="o", ms=4, color=BLUE, ecolor=BLUE, elinewidth=1, capsize=0)
    axes[0].set_yticks(y, base.group)
    axes[0].set_xlabel("Baseline MSO, 2015 to Nov 2022 (%)")
    e = np.array([100 * d[k] for d in ex])
    lo = np.array([100 * d["excess_lo"] for d in ex])
    hi = np.array([100 * d["excess_hi"] for d in ex])
    axes[1].errorbar(e, y, xerr=[e - lo, hi - e], fmt="o", ms=4, color=BLUE, ecolor=BLUE, elinewidth=1, capsize=0)
    axes[1].axvline(0, color=MUTED, lw=0.6)
    axes[1].set_xlabel(f"Excess over pre-trend, {k[-7:]} (pp)")
    fig.tight_layout()
    fig.savefig(FIG / "fields.pdf")


def fig_learners():
    a = pd.read_csv(RES / "essay_mso_by_group.csv").set_index("group")
    b = pd.read_csv(RES / "essay_embedding_instrument.csv").set_index("group")
    fig, ax = plt.subplots(figsize=(3.0, 1.6))
    for i, (name, df) in enumerate([("Style features (primary)", a), ("Sentence embeddings", b)]):
        for j, (g, c) in enumerate([("non-ELL", BLUE), ("ELL", ORANGE)]):
            r = df.loc[g]
            yy = i + (0.15 if j == 0 else -0.15)
            ax.errorbar(100 * r.mso, yy, xerr=[[100 * (r.mso - r.lo)], [100 * (r.hi - r.mso)]], fmt="o", ms=4,
                        color=c, ecolor=c, elinewidth=1, capsize=0, label=g if i == 0 else None)
    ax.set_yticks([0, 1], ["Style features\n(primary)", "Sentence\nembeddings"])
    ax.set_xlabel("MSO (%)")
    ax.legend(loc="lower right", fontsize=6.5)
    fig.tight_layout()
    fig.savefig(FIG / "learners.pdf")


if __name__ == "__main__":
    FIG.mkdir(parents=True, exist_ok=True)
    for f in (fig_learners, fig_timeseries, fig_fields):
        try:
            f()
            print("ok", f.__name__)
        except FileNotFoundError as e:
            print("skip", f.__name__, "(missing", Path(e.filename).name + ")")
