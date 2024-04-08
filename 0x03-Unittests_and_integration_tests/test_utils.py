#!/usr/bin/env python3
"""
Test module for utils module
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
    Union
)
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for access nested map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            result: Union[Dict, int]
            ) -> None:
        """Test utils.access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            err: Exception
            ) -> None:
        """ Test for exceptions """
        with self.assertRaises(err):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Class for get_json
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict
            ) -> None:
        """
        Mock HTTP calls
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req:
            self.assertEqual(get_json(test_url), test_payload)
            req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test class for utils.memoize
    """

    def test_memoize(self) -> None:
        """
        Test method for memoize
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                    TestClass,
                    "a_method",
                    return_value=lambda: 42
                ) as memo:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo.assert_called_once()
