"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: had to look at old HW for binary search algo reminder.
"""
def min_rotated(nums: list) -> int:
    """function to get the minimum of a sorted array in logn time"""
    begin, end = 0, len(nums) - 1
    while begin < end:
        mid = begin +(end-begin) // 2
        if nums[mid] > nums[end]:
            begin = mid + 1
        else:
            end = mid
    return nums[begin]
#End-of-file (EOF)
