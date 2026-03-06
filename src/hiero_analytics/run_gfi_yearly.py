from __future__ import annotations

from hiero_analytics.config.paths import ensure_output_dirs, DATA_DIR, CHARTS_DIR
from hiero_analytics.data_sources.github_client import GitHubClient
from hiero_analytics.data_sources.github_graphql import fetch_org_issues_graphql
from hiero_analytics.identity.issue_normalizer import normalize_issues
from hiero_analytics.transform.dataframe import issues_to_dataframe
from hiero_analytics.metrics.good_first_issue import good_first_issue_metrics
from hiero_analytics.metrics.plotting.domain import (
    plot_gfi_yearly_trend,
    plot_gfi_total_by_repo,
    plot_gfi_yearly_distribution,
)


ORG = "hiero-ledger"


def main() -> None:
    """
    Run Good First Issue analytics pipeline.
    """
    ensure_output_dirs()

    print(f"Running Good First Issue analytics for org: {ORG}")

    client = GitHubClient()

    raw = fetch_org_issues_graphql(client, org=ORG)

    print(f"Fetched {len(raw)} raw issues")

    issues = normalize_issues(raw)

    print(f"Normalized {len(issues)} issues")

    df = issues_to_dataframe(issues)

    metrics = good_first_issue_metrics(df)

    yearly = metrics["yearly"]
    yearly_by_repo = metrics["yearly_by_repo"]
    total_by_repo = metrics["total_by_repo"]

    total_by_repo = total_by_repo.sort_values("count", ascending=False)


    yearly.to_csv(DATA_DIR / "gfi_yearly.csv", index=False)
    yearly_by_repo.to_csv(DATA_DIR / "gfi_yearly_by_repo.csv", index=False)
    total_by_repo.to_csv(DATA_DIR / "gfi_total_by_repo.csv", index=False)

    print("Saved analytics tables")

    plot_gfi_yearly_trend(
        yearly,
        CHARTS_DIR / "gfi_yearly_line.png",
    )

    plot_gfi_total_by_repo(
        total_by_repo,
        CHARTS_DIR / "gfi_total_by_repo.png",
    )

    plot_gfi_yearly_distribution(
        yearly,
        CHARTS_DIR / "gfi_yearly.png",
    )

    print("Charts generated")
    print("Analytics pipeline completed")


if __name__ == "__main__":
    main()