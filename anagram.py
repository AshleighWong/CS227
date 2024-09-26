"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""

def anagram(word_1: str, word_2: str) -> bool:
    """Function to check if two words are anagrams."""
    dic = {}
    for i in word_1.lower():
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in word_2.lower():
        if i not in dic:
            return False
        dic[i] -= 1
    for value in dic.values():
        if value != 0:
            return False
    return True
#End-of-file (EOF)
