"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""
from typing import List
from collections import deque

def checkout_lines(carts: List[int]) -> int:
    """Function using dequeue to process customer carts and checkout"""
    time = 0
    checkers = [0, 0, 0]
    queue = deque(carts)
    while queue or 0 in checkers:
        for i in range(3):
            if checkers[i] == 0 and queue:
                checkers[i] = queue.popleft()
        checkers = [max(0, count - 1) for count in checkers]
        time += 1
    return time
#End-of-file (EOF)
