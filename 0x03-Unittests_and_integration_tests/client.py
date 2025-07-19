#!/usr/bin/env python3
"""GithubOrgClient module."""

import requests


def get_json(url: str) -> dict:
    """Make a GET request and return the JSON response."""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


class GithubOrgClient:
    """Client to interact with the Github organization API."""

    def __init__(self, org_name: str):
        self.org_name = org_name

    @property
    def org(self) -> dict:
        """Return the organization JSON data."""
        return get_json(f"https://api.github.com/orgs/{self.org_name}")

    @property
    def _public_repos_url(self) -> str:
        """Return the repos_url from the organization data."""
        return self.org.get("repos_url", "")

    def public_repos(self, license: str = None) -> list[str]:
        """Return list of public repo names.

        If license is specified, filter repos by license key.
        """
        repos = get_json(self._public_repos_url)
        repo_names = []
        for repo in repos:
            if license is None or self.has_license(repo, license):
                repo_names.append(repo.get("name"))
        return repo_names

    def has_license(self, repo: dict, license_key: str) -> bool:
        """Check if a repo has a specific license key."""
        license = repo.get("license")
        if license is None:
            return False
        return license.get("key") == license_key
