"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""

def median_5(nums: list) -> int:
    """get the median of a list with length <=5"""
    length = len(nums)
    nums.sort()
    half = length//2
    if length%2 == 0:
        return nums[half]
    return nums[half]
#End-of-file (EOF)
