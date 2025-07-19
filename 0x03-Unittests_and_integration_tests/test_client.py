#!/usr/bin/env python3
"""Tests for client.GithubOrgClient"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the expected payload."""
        mock_get_json.return_value = {"org": org_name}
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once()
        self.assertEqual(result, {"org": org_name})

    def test_public_repos_url(self):
        """Test that _public_repos_url returns expected URL from org data."""
        client = GithubOrgClient("test_org")
        with patch.object(
            GithubOrgClient,
            "org",
            new_callable=unittest.mock.PropertyMock,
            return_value={"repos_url": "https://api.github.com/orgs/test_org/repos"},
        ):
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/test_org/repos"
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns expected repo list."""
        test_repos = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_repos
        client = GithubOrgClient("test_org")
        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=unittest.mock.PropertyMock,
            return_value="https://api.github.com/orgs/test_org/repos"
        ):
            repos = client.public_repos()
            self.assertEqual(repos, ["repo1", "repo2"])
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license returns True if license_key matches repo license."""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (
            fixtures.org_payload,
            fixtures.repos_payload,
            fixtures.expected_repos,
            fixtures.apache2_repos,
        )
    ],
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Mock requests.get to return fixture data based on URL."""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url, *args, **kwargs):
            mock_resp = Mock()
            if url.endswith("/repos"):
                mock_resp.json.return_value = cls.repos_payload
            else:
                mock_resp.json.return_value = cls.org_payload
            return mock_resp

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patching requests.get."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected repos."""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test filtering repos by license key."""
        client = GithubOrgClient("test_org")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
