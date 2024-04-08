#!/usr/bin/env python3
"""
Test client module
"""
import unittest
from unittest.mock import (
    patch,
    MagicMock
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
