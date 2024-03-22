#!/usr/bin/env python3
""" Async """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Random """
    wait_seconds: float = random.random() * max_delay
    await asyncio.sleep(wait_seconds)
    return wait_seconds
