#!/usr/bin/env python3
"""
Test module for utils module
"""
import unittest
import utils
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
    Union
)


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
        self.assertEqual(utils.access_nested_map(nested_map, path), result)

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
            utils.access_nested_map(nested_map, path)
