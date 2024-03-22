#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
from asyncio import Task
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Tasks
    """
    result: List[float] = []
    tasks: List[Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        result.append(await task)

    return result
