#!/usr/bin/env python3
"""
Parallel comprehensions
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    4 Parallel comprehensions
    """
    start = time.time()

    batch = asyncio.gather(async_comprehension(),
                           async_comprehension(),
                           async_comprehension(),
                           async_comprehension())

    list1, list2, list3, list4 = await batch

    return time.time() - start
