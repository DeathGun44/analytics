from __future__ import annotations

import pandas as pd


def build_gfi_pipeline(
    gfi_yearly: pd.DataFrame,
    gfic_yearly: pd.DataFrame,
) -> pd.DataFrame:
    """
    Build a yearly onboarding pipeline dataset.

    Combines Good First Issue (GFI) and Good First Issue Candidate (GFIC)
    counts into a single dataframe suitable for stacked charts.

    Returns
    -------
    pd.DataFrame
        Columns:
        - year
        - gfi
        - gfic
    """

    pipeline = (
        gfi_yearly.rename(columns={"count": "gfi"})
        .merge(
            gfic_yearly.rename(columns={"count": "gfic"}),
            on="year",
            how="outer",
        )
        .fillna(0)
    )

    pipeline[["gfi", "gfic"]] = pipeline[["gfi", "gfic"]].astype(int)

    return pipeline.sort_values("year")


def build_onboarding_repo_pipeline(
    gfi_total_by_repo: pd.DataFrame,
    gfic_total_by_repo: pd.DataFrame,
) -> pd.DataFrame:
    """
    Build onboarding pipeline dataset grouped by repository.

    Returns
    -------
    pd.DataFrame
        Columns:
        - repo
        - gfi
        - gfic
    """

    pipeline = (
        gfi_total_by_repo.rename(columns={"count": "gfi"})
        .merge(
            gfic_total_by_repo.rename(columns={"count": "gfic"}),
            on="repo",
            how="outer",
        )
        .fillna(0)
    )

    pipeline[["gfi", "gfic"]] = pipeline[["gfi", "gfic"]].astype(int)

    return pipeline.sort_values("gfi", ascending=False)