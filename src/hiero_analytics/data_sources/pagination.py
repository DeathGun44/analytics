"""
This module provides generic pagination functions for APIs that use page numbers or cursor-based pagination. 
These functions can be used to fetch all items from an API endpoint that supports pagination, abstracting away the details of how pagination works for that specific API.
The `paginate_page_number` function is designed for APIs that use page numbers, while the `paginate_cursor` function is designed for APIs that use cursors (such as GraphQL)."""
from __future__ import annotations

from typing import Callable, List, Any, Tuple


DEFAULT_PAGE_SIZE = 100


def paginate_page_number(
    fetch_page: Callable[[int], list[Any]],
    page_size: int = DEFAULT_PAGE_SIZE,
) -> List[Any]:
    """
    Collect items from a page-number-based API.

    The callback should return a list of items for the requested page.
    Pagination stops when an empty page is returned.
    """

    results: List[Any] = []
    page = 1

    while True:

        items = fetch_page(page)

        if not items:
            break

        results.extend(items)

        if len(items) < page_size:
            break

        page += 1

    return results


def paginate_cursor(
    fetch_page: Callable[[str | None], Tuple[list[Any], str | None, bool]],
) -> List[Any]:
    """
    Generic paginator for cursor-based APIs such as GraphQL.

    fetch_page(cursor) must return:
        (items, next_cursor, has_next_page)
    """

    results: List[Any] = []
    cursor: str | None = None

    while True:

        items, next_cursor, has_next = fetch_page(cursor)

        results.extend(items)

        if not has_next:
            break

        cursor = next_cursor

    return results