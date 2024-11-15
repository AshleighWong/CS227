"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: had to search for the condensed swap method
"""
def sort_by_parity(nums):
    """function to move all evens to front of array and odd to the back"""
    begin, end = 0, len(nums)-1
    while begin < end:
        if nums[begin] % 2 == 0:
            begin +=1
        if nums[end] % 2 == 1:
            end -=1
        else:
            nums[begin], nums[end] = nums[end], nums[begin]
    return nums
#End-of-file (EOF)
