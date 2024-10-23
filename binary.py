"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""
def binary_search(cards, min_ind, max_ind, target):
    """binary search function"""
    while min_ind <= max_ind:
        mid = min_ind + (max_ind-min_ind)//2
        curr = cards[mid]
        if curr == target:
            return True
        if curr < target:
            min_ind = mid+1
        else:
            max_ind = mid-1
    return False
#End-of-file (EOF)
