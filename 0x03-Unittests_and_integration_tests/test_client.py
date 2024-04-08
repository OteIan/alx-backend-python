#!/usr/bin/env python3
"""
Test client module
"""
import unittest
from unittest.mock import (
    patch,
    MagicMock,
    PropertyMock
)
from typing import Dict
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test GithubOrg client class
    """
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch("client.get_json")
    def test_org(
                self,
                org: str,
                response: Dict,
                mocked_fn: MagicMock
            ) -> None:
        """
        Tests the 'org' method
        """
        mocked_fn.return_value = MagicMock(return_value=response)
        gthub_org_client = GithubOrgClient(org)
        self.assertEqual(gthub_org_client.org(), response)

        mocked_fn.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self) -> None:
        """
        Tests the '_public_repos_url' method
        """
        with patch(
                    "client.GithubOrgClient.org",
                    new_callable=PropertyMock
                ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
                }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/orgs/google/repos"
            )
