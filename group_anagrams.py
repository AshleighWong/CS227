"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements
"""
from collections import defaultdict
def group_anagram(strs: list) -> list:
    """
    Function group anagrams in a list and return the groups in a list
    """
    if len(strs) <= 1:
        return [strs[0]]
    groups = defaultdict(list)
    for word in strs:
        key = ''.join(sorted(word))
        groups[key].append(word)
    result = list(groups.values())
    return result
#End-of-file (EOF)
