"""
Defines configuration constants for GitHub API interactions in the analytics module.
Includes settings for API endpoints, authentication, and rate limiting to ensure efficient and reliable data retrieval from
"""
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
BASE_URL = "https://api.github.com"

# Delays the time between API requests 
# Hardcoded - not yet a sophisticated rate limiter
HTTP_TIMEOUT_SECONDS = 10
REQUEST_DELAY_SECONDS = 0.25

def github_headers() -> dict[str, str]:
    """
    Returns the HTTP headers for GitHub requests, including the Authorization header if a GITHUB_TOKEN is provided in the environment variables.
    This is used to authenticate requests to the GitHub API and can help increase rate limits for authenticated requests.

    Used for all GitHub API interactions in the analytics module to ensure consistent authentication handling across requests.

    Args:
        None (reads GITHUB_TOKEN from environment variables)
    Returns:
        A dictionary of HTTP headers to include in GitHub API requests, with the Authorization header if GITHUB_TOKEN is set.
    """
    if not GITHUB_TOKEN:
        logger.warning("GITHUB_TOKEN not set. Rate limit: 60 requests/hour.")
    if GITHUB_TOKEN:
        logger.info("Using GITHUB_TOKEN for authenticated requests. API allows up to 5000 requests per hour.")
        return {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    return {}