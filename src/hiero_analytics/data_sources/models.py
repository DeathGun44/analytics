"""
This module defines data models for representing GitHub issues and repositories. 
These models are used to structure the data fetched from the GitHub API and make it easier to work with in the rest of the application.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class IssueRecord:
    repo: str
    number: int
    title: str
    state: str
    created_at: datetime
    labels: List[str]


@dataclass
class RepoRecord:
    full_name: str