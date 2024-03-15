#!/usr/bin/env python3
""" Duck types """
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Duck types """
    return [(i, len(i)) for i in lst]
