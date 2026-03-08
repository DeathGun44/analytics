"""
Chart title generators from labels for easier and consistent formatting across charts.
"""
def label_yearly(label: str) -> str:
    """
    Args:
        label: The base label for the chart (e.g., "Commits", "Issues", "Pull Requests").
    Returns:
        A formatted chart title string that includes the label and indicates that the data is aggregated by year
    
    Example: "Commits per Year", "Issues per Year", "Pull Requests per Year
    """
    return f"{label} per Year"


def label_total_by_repo(label: str) -> str:
    """
    Args:
        label: The base label of interest (e.g., "Good First Issues", "Contributors", "Pull Requests").
    Returns:
        A formatted chart title string that includes the label and indicates that the data is aggregated by repository
    
    Example: "Good First Issues by Repository", "Contributors by Repository", "Pull Requests by Repository"
    """
    return f"{label} by Repository"


def pipeline(label_a: str, label_b: str) -> str:
    """
    Args:        
        label_a: The base label for the first stage of the pipeline (e.g., "Issues", "Pull Requests").
        label_b: The base label for the second stage of the pipeline (e.g., "Closed Issues", "Merged Pull Requests").
    Returns:
        A formatted chart title string that includes both labels and indicates a pipeline relationship between them.
    Example: "Issues → Closed Issues Pipeline", "Pull Requests → Merged Pull Requests Pipeline"
    """
    return f"{label_a} → {label_b} Pipeline"