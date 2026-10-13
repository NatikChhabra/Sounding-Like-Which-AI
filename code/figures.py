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
PDF_META = {"CreationDate": None}  # no timestamp: rebuilding unchanged figures leaves the files unchanged

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
        ax.legend(loc="upper left", fontsize=5.6, framealpha=0.9, facecolor="white",
                  frameon=True, edgecolor="none")


def fig_timeseries():
    fig, axes = plt.subplots(1, 3, figsize=(6.6, 2.3), sharex=True)
    its_panel(axes[0], "arxiv_monthly", BLUE, "arXiv", legend=True)
    axes[0].set_title("(a) MSO, arXiv abstracts", fontsize=8, color=INK, loc="left")
    axes[0].set_ylim(top=72)  # legend sits above the data
    its_panel(axes[1], "hansard_monthly", ORANGE, "Hansard")
    axes[1].set_title("(b) MSO, parliamentary speech", fontsize=8, color=INK, loc="left")
    its_panel(axes[2], "arxiv_marker_monthly", AQUA, "arXiv", ylabel="Abstracts with marker word (%)")
    axes[2].set_title("(c) Marker words, arXiv", fontsize=8, color=INK, loc="left")
    for ax in axes:
        ax.tick_params(axis="x", labelsize=6.5)
        ax.xaxis.set_major_locator(matplotlib.dates.YearLocator(3))
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y"))
    fig.tight_layout()
    fig.savefig(FIG / "timeseries.pdf", metadata=PDF_META)


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
    axes[0].set_yticks(y, [f"{g} ({n:,})" for g, n in zip(base.group, base.n)])
    axes[0].set_xlabel("Baseline MSO (%)", fontsize=7)
    axes[0].set_xlim(left=0)
    e = np.array([100 * d[k] for d in ex])
    lo = np.array([100 * d["excess_lo"] for d in ex])
    hi = np.array([100 * d["excess_hi"] for d in ex])
    axes[1].errorbar(e, y, xerr=[e - lo, hi - e], fmt="o", ms=4, color=BLUE, ecolor=BLUE, elinewidth=1, capsize=0)
    axes[1].axvline(0, color=MUTED, lw=0.6)
    axes[1].set_xlabel("Gap, June 2025 (pp)", fontsize=7)
    for ax in axes:
        ax.tick_params(labelsize=6.5)
    fig.subplots_adjust(left=0.29, right=0.98, bottom=0.2, top=0.97)
    fig.savefig(FIG / "fields.pdf", metadata=PDF_META)


def fig_learners():
    inst = [("Style features\n(primary)", "essay_mso_by_group"), ("Sentence\nembeddings", "essay_embedding_instrument"),
            ("Perplexity, GPT-2\n(detector-style)", "essay_perplexity_instrument_gpt2")]
    inst = [(n, pd.read_csv(RES / f"{f}.csv").set_index("group")) for n, f in inst if (RES / f"{f}.csv").exists()]
    fig, ax = plt.subplots(figsize=(3.1, 0.6 + 0.55 * len(inst)))
    for i, (name, df) in enumerate(inst[::-1]):
        for j, (g, c) in enumerate([("non-ELL", BLUE), ("ELL", ORANGE)]):
            r = df.loc[g]
            yy = i + (0.15 if j == 0 else -0.15)
            ax.errorbar(100 * r.mso, yy, xerr=[[100 * (r.mso - r.lo)], [100 * (r.hi - r.mso)]], fmt="o", ms=4,
                        color=c, ecolor=c, elinewidth=1, capsize=0, label=g if i == 0 else None)
    ax.set_yticks(range(len(inst)), [n for n, _ in inst[::-1]], fontsize=6.5)
    ax.set_xlabel("Held-out essays flagged as LLM-like (%)", fontsize=7)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.32), ncol=2, fontsize=6.5)
    fig.tight_layout()
    fig.savefig(FIG / "learners.pdf", metadata=PDF_META)


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
    fig.savefig(FIG / "gensets.pdf", metadata=PDF_META)


# generators in release order (year of release; RAID's are 2023 systems)
VINTAGE = [("raid-cohere-chat", "Cohere command", 2023), ("raid-mpt-chat", "MPT-30B-chat", 2023),
           ("raid-llama-chat", "Llama-2-Chat 70B", 2023), ("raid-mistral-chat", "Mistral-7B-Instr. v0.1", 2023),
           ("raid-chatgpt", "ChatGPT", 2023), ("raid-gpt4", "GPT-4", 2023), ("llama2:7b", "Llama-2-Chat 7B", 2023),
           ("vicuna:7b", "Vicuna 7B v1.5", 2023), ("mistral:7b", "Mistral 7B v0.3", 2024),
           ("llama3.1:8b", "Llama 3.1 8B", 2024), ("phi4:14b", "Phi-4 14B", 2024), ("gemma3:12b", "Gemma 3 12B", 2025),
           ("granite3.3:8b", "Granite 3.3 8B", 2025), ("qwen3:8b", "Qwen3 8B", 2025), ("gpt-oss:20b", "gpt-oss 20B", 2025),
           ("qwen3.5:9b", "Qwen3.5 9B", 2026), ("gemma4:12b", "Gemma 4 12B", 2026),
           ("granite4.2:8b", "Granite 4.2 8B", 2026), ("claude-opus-5.5", "2026 model", 2026)]
YEAR_COLOR = {2023: "#e87ba4", 2024: "#8b5cf6", 2025: AQUA, 2026: ORANGE}


def fig_vintage():
    v = pd.read_csv(RES / "arxiv_vintage.csv").set_index("group")
    years = [int(c[1:]) for c in v.columns if c.startswith("y")]
    fig, (a, b) = plt.subplots(1, 2, figsize=(6.6, 2.4), gridspec_kw={"width_ratios": [1, 1.25]})
    sets = [("pre2022data_matched", "Pre-ChatGPT pretraining data", BLUE, "-"),
            ("raid_all", "RAID 2023 chat models", YEAR_COLOR[2023], "-"),
            ("local_p1", "Open models 2024\u201325 (incl. gpt-oss)", YEAR_COLOR[2025], "-"),
            ("single:gpt-oss:20b", "gpt-oss (Aug 2025)", YEAR_COLOR[2025], "--"),
            ("open2026_p1", "Open models 2026", YEAR_COLOR[2026], "--"),
            ("frontier_p1", "2026 model (Claude Opus 5.5)", YEAR_COLOR[2026], "-")]
    for k, label, c, ls in sets:
        if k in v.index:
            a.plot(years, [100 * v.loc[k, f"y{y}"] for y in years], color=c, lw=1.8, ls=ls, marker="o", ms=2.5,
                   label=label)
    a.axvline(2022.9, color=INK, lw=0.6)
    a.set_ylabel("arXiv MSO (%)")
    a.set_xticks([2015, 2018, 2021, 2024, 2026])
    a.set_ylim(0, 62)  # headroom so the legend clears the 2026-model line
    a.legend(fontsize=5.6, loc="upper left")
    a.set_title("(a) MSO by reference set", fontsize=7.5, loc="left")
    # (b) quarter of peak single-generator MSO against the generator's release date
    import analysis  # release months live with the analysis code
    q = pd.read_csv(RES / "arxiv_vintage_quarterly.csv").set_index("group")
    pk = pd.PeriodIndex(q.peak, freq="Q")
    q["peak_x"] = pk.year + (pk.quarter - 1) / 4 + 0.125
    label = {m: lab for m, lab, _ in VINTAGE}
    show = {"raid-gpt4", "raid-cohere-chat", "vicuna:7b", "phi4:14b", "gpt-oss:20b", "qwen3.5:9b", "gemma4:12b", "granite4.2:8b"}
    seen = {}
    for g, r in q.iterrows():
        m = g[7:]
        key = (analysis.RELEASE.get(m), r.peak_x)
        r = r.copy()
        r["peak_x"] += 0.05 * seen.get(key, 0)  # offset points that would coincide
        seen[key] = seen.get(key, 0) + 1
        yr = next(y for mm, _, y in VINTAGE if mm == m)
        if m in analysis.RELEASE:
            x = analysis.RELEASE[m]
            b.scatter(x, r.peak_x, s=16, color=YEAR_COLOR[yr], zorder=3)
            if m in show:
                text = "Gemma 3, Granite 3.3,\nQwen3 (2025Q4)" if m == "qwen3:8b" else label[m]  # one label, three points
                off, ha, va = {"gemma4:12b": ((3, -7), "left", "baseline"), "qwen3.5:9b": ((-5, -1), "right", "center"),
                               "qwen3:8b": ((-4, -6), "center", "top"),
                               "gpt-oss:20b": ((-4, 2), "right", "bottom")}.get(m, ((3, 2), "left", "baseline"))
                b.annotate(text, (x, r.peak_x), xytext=off, ha=ha, va=va, linespacing=0.95,
                           textcoords="offset points", fontsize=6, color=MUTED)
        else:  # release month not public: drawn in a separate "n/a" column; peak right-censored at the last quarter
            b.scatter(2027.0, r.peak_x, s=16, facecolors="none", edgecolors=YEAR_COLOR[yr], zorder=3)
            b.annotate("2026 model\n(still rising)", (2027.0, r.peak_x), xytext=(0, 5), ha="center", va="bottom",
                       linespacing=0.95, textcoords="offset points", fontsize=6, color=MUTED)
    rho = json.loads((RES / "arxiv_vintage_peak.json").read_text())
    b.text(0.2, 0.34, f"Spearman $\\rho$ = {rho['rho']:.2f} (n = {rho['n']}; 2026 model excluded)",
           transform=b.transAxes, fontsize=6, va="top", color=INK)
    for yr, c in YEAR_COLOR.items():
        b.scatter([], [], s=16, color=c, label=str(yr))
    b.legend(fontsize=5.6, title="Released", title_fontsize=5.6, loc="lower right", ncol=2)
    b.set_xlabel("Generator release date")
    b.set_ylabel("Quarter of peak MSO")
    b.set_xticks([2024, 2025, 2026, 2027.0], ["2024", "2025", "2026", "n/a"])
    years = range(int(q.peak_x.min()), 2027)  # every peak on the axis, however early
    ticks = [y + (k - 1) / 4 + 0.125 for y in years for k in (1, 3)]
    b.set_yticks(ticks, [f"{y}Q{k}" for y in years for k in (1, 3)])
    b.set_ylim(q.peak_x.min() - 0.3, 2027.25)
    b.set_title("(b) Single-generator regions", fontsize=7.5, loc="left")
    fig.tight_layout()
    fig.savefig(FIG / "vintage.pdf", metadata=PDF_META)


if __name__ == "__main__":
    FIG.mkdir(parents=True, exist_ok=True)
    for f in (fig_learners, fig_timeseries, fig_fields, fig_gensets, fig_vintage):
        try:
            f()
            print("ok", f.__name__)
        except FileNotFoundError as e:
            print("skip", f.__name__, "(missing", Path(e.filename).name + ")")
