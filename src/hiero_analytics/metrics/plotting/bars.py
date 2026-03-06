from __future__ import annotations

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
from pathlib import Path

from .base import create_figure, finalize_chart


def plot_bar(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str,
    output_path: Path,
) -> None:
    """
    Plot a simple bar chart from a dataframe.
    """

    if df.empty:
        raise ValueError("DataFrame is empty. Cannot plot bar chart.")

    # Sort for readability if categorical
    if x_col == "repo":
        df = df.sort_values(y_col, ascending=False)

    create_figure()

    # Generate distinct colors
    colors = cm.tab20(np.linspace(0, 1, len(df)))

    plt.bar(
        df[x_col],
        df[y_col],
        color=colors,
    )

    rotate = 45 if x_col == "repo" else None

    finalize_chart(
        title=title,
        xlabel=x_col,
        ylabel=y_col,
        output_path=output_path,
        rotate_x=rotate,
    )