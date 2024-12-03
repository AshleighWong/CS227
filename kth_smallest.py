"""
Name: Ashleigh Wong
Email: ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of heapq methods.
"""

import heapq

def kth_smallest(nums, kth=1):
    """
    Find the kth smallest element in a list using a min-heap.
    """
    heapq.heapify(nums)
    for _ in range(kth):
        result = heapq.heappop(nums)
    return result
