from __future__ import annotations

import matplotlib.pyplot as plt

from hiero_analytics.config.charts import (
    DEFAULT_FIGSIZE,
)

# Global style parameters
CHART_STYLE = "seaborn-v0_8-whitegrid"

FONT_SIZE_TITLE = 14
FONT_SIZE_LABEL = 11
FONT_SIZE_TICKS = 10
FONT_SIZE_LEGEND = 10


def apply_style() -> None:
    """
    Apply consistent matplotlib styling for all analytics charts.
    """

    plt.style.use(CHART_STYLE)

    plt.rcParams.update(
        {
            "figure.figsize": DEFAULT_FIGSIZE,
            "figure.autolayout": True,
            "axes.titlesize": FONT_SIZE_TITLE,
            "axes.labelsize": FONT_SIZE_LABEL,
            "xtick.labelsize": FONT_SIZE_TICKS,
            "ytick.labelsize": FONT_SIZE_TICKS,
            "legend.fontsize": FONT_SIZE_LEGEND,
            "axes.grid": True,
            "grid.alpha": 0.4,
            "grid.linestyle": "--",
        }
    )
