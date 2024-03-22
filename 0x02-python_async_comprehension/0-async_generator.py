#!/usr/bin/env python3
"""
Async Generator
"""
import random
import asyncio


async def async_generator():
    """
    Yields a random number btwn 1 & 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        time: float = random.uniform(0, 10)
        yield time
