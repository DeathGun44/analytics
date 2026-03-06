"""
A wrapper around plotting functions for the Good First Issues metrics."""
from __future__ import annotations

from pathlib import Path
import pandas as pd

from .bars import plot_bar
from .lines import plot_line


def plot_gfi_yearly_trend(
    yearly: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot Good First Issues trend over time.
    """

    if yearly.empty:
        return

    plot_line(
        yearly,
        x_col="year",
        y_col="count",
        title="Good First Issues per Year",
        output_path=output_path,
    )


def plot_gfi_total_by_repo(
    total_by_repo: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot total Good First Issues per repository.
    """

    if total_by_repo.empty:
        return

    plot_bar(
        total_by_repo,
        x_col="repo",
        y_col="count",
        title="Total Good First Issues by Repository",
        output_path=output_path,
    )


def plot_gfi_yearly_distribution(
    yearly: pd.DataFrame,
    output_path: Path,
) -> None:
    """
    Plot yearly distribution of Good First Issues.
    """

    if yearly.empty:
        return

    plot_bar(
        yearly,
        x_col="year",
        y_col="count",
        title="Good First Issues per Year",
        output_path=output_path,
    )