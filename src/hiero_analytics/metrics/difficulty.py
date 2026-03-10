from __future__ import annotations

import pandas as pd

from hiero_analytics.domain.difficulty import DIFFICULTY_LEVELS


def difficulty_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute difficulty distribution for issues.

    Parameters
    ----------
    df : pd.DataFrame
        Issue dataframe containing a "labels" column.

    Returns
    -------
    pd.DataFrame
        Columns:
            difficulty
            count
    """

    if df.empty:
        return pd.DataFrame(columns=["difficulty", "count"])

    rows = []

    for level in DIFFICULTY_LEVELS:

        mask = df["labels"].map(level.label_spec.matches)

        rows.append(
            {
                "difficulty": level.name,
                "count": int(mask.sum()),
            }
        )

    return pd.DataFrame(rows)


def merged_pr_difficulty_distribution(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Compute difficulty distribution for merged pull requests.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing PR-linked issue labels.

    Returns
    -------
    pd.DataFrame
        Columns:
            difficulty
            count
    """

    return difficulty_distribution(df)