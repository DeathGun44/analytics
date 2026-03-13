"""Logging configuration for hiero_analytics.

This module centralizes basic logging setup for the application. The
log level can be configured via the ``LOG_LEVEL`` environment variable;
if it is not set, the default level ``INFO`` is used.
"""
import logging
import os

def setup_logging() -> None:
    """Configure basic application logging.

    The log level is determined by the ``LOG_LEVEL`` environment variable
    (e.g. ``DEBUG``, ``INFO``, ``WARNING``, ``ERROR``, ``CRITICAL``) and
    defaults to ``INFO`` if unset. Log messages use a simple format that
    includes the timestamp, level name, and message.
    """
    level = os.getenv("LOG_LEVEL", "INFO").upper()

    logging.basicConfig(
        level=getattr(logging, level),
        format="%(asctime)s | %(levelname)s | %(message)s",
    )