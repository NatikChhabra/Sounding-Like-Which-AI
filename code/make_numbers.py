"""results/*.json|csv -> results/numbers.tex. The paper cites numbers only as \\R{file.row.column};
a missing key is a LaTeX error, so text and results cannot drift apart.
"""
import json, math
from pathlib import Path

import pandas as pd

RES = Path(__file__).resolve().parent.parent / "results"
PCT = ("mso", "recall", "share", "excess", "level_shift", "slope_change", "pre_slope", "lo", "hi", "difference")
KEYCOLS = ("group", "held_out_model", "feature", "fake_break")


def fmt(key, v):
    leaf = key.rsplit(".", 1)[-1]
    if isinstance(v, str):
        return v.replace("_", r"\_").replace("&", r"\&")
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "--"
    if leaf.startswith("p") and (leaf == "p" or leaf.endswith("_p") or leaf == "p_value"):
        return r"{<}0.001" if v < 0.001 else f"{v:.3f}"
    if leaf in ("n", "months", "n_train_per_class", "dof"):
        return f"{int(v):,}"
    if leaf.startswith(("or_", "odds")):
        return f"{v:.2f}"
    if "auc" in leaf:
        return f"{v:.3f}"
    if leaf.startswith(PCT) or leaf.endswith(PCT):
        return f"{100 * v:.1f}"  # percentage points, no % sign (added in text)
    return f"{v:.2f}"


def flatten(prefix, obj, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            flatten(f"{prefix}.{k}", v, out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            name = v.get("fake_break", i) if isinstance(v, dict) else i
            flatten(f"{prefix}.{name}", v, out)
    else:
        out[prefix] = fmt(prefix, obj)


def main():
    out = {}
    for f in sorted(RES.glob("*.json")):
        flatten(f.stem, json.loads(f.read_text()), out)
    for f in sorted(RES.glob("*.csv")):
        df = pd.read_csv(f)
        if "model" in df and "prompt" in df:
            df.index = df.model.astype(str) + "/" + df.prompt.astype(str)
        else:
            col = next((c for c in KEYCOLS if c in df), None)
            if col is None:
                continue  # time series: figures only
            df.index = df[col].astype(str)
        for row, r in df.iterrows():
            for c, v in r.items():
                flatten(f"{f.stem}.{row}.{c}", v, out)
    lines = [r"\newcommand{\R}[1]{\ifcsname r@#1\endcsname\csname r@#1\endcsname\else"
             r"\errmessage{Missing result #1}\fi}"]
    lines += [rf"\expandafter\def\csname r@{k}\endcsname{{{v}}}" for k, v in sorted(out.items())]
    (RES / "numbers.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(len(out), "numbers")


if __name__ == "__main__":
    assert fmt("x.mso", 0.0351) == "3.5" and fmt("x.p_value", 0.0001) == r"{<}0.001"
    assert fmt("x.odds_ratio", 0.356) == "0.36" and fmt("x.n", 7424) == "7,424"
    assert fmt("x.or_lo", 0.1656) == "0.17" and fmt("x.cv_auc_all", 0.98763) == "0.988"
    main()
