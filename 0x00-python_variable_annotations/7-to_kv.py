#!/usr/bin/env python3
""" string & int/float to tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ To tuple """
    return (k, v ** 2)
