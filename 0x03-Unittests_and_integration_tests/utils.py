#!/usr/bin/env python3
"""Utils module."""

from typing import Any, Tuple
import requests


def access_nested_map(nested_map: dict, path: Tuple) -> Any:
    """Access nested map with a sequence of keys."""
    current = nested_map
    for key in path:
        current = current[key]
    return current


def get_json(url: str) -> dict:
    """Get JSON content from URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def memoize(fn):
    """Decorator to memoize a method's result."""

    def wrapper(self):
        attr_name = f"_{fn.__name__}"
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(wrapper)
