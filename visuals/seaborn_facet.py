"""
Create a seaborn facet chart with individual custom annotations.
"""

from typing import List

import pandas as pd
import seaborn as sns


def plot_dist(df: pd.DataFrame, var_name: str, order: List[str]) -> sns.axisgrid.FacetGrid:
    
    # Create the entire chart.
    dp = df[(df[var_name] >= 0) & (df[var_name].notna())].copy()
    g = sns.FacetGrid(dp, col="scope", hue="pg_rollup", col_wrap=2, col_order = order)
    g.map(sns.ecdfplot, var_name)
    g.add_legend(title="")

    # Customize the individual subplots
    for s, ax in g.axes_dict.items():
        
        ds = df.loc[d["scope"] == s, :]
        dps = dp.loc[dp["scope"] == s, :]
        
        # Title
        data_prop = dps.shape[0] / ds[ds["tip1_bin"]].shape[0]
        ax.set_title(f"{s} ({data_prop:.2f})")
        
        # Reference lines
        p50, p90 = dps[var_name].quantile([.5, .9]).values
        ax.axvline(p50, color = "grey", linestyle="dashed")
        ax.text(p50 + .5, .05, f'{p50:.0f}', rotation = 90)
        ax.axvline(p90, color = "grey", linestyle="dashed")
        ax.text(p90 + .5, .05, f'{p90:.0f}', rotation = 90) 
    return g
