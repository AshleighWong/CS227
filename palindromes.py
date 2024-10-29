"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""
from collections import deque
def is_palindrome(input_s: str):
    """Function using dequeue to check for palindrome with only alphanum"""
    que = deque()
    for char in input_s.lower().replace(' ', ''):
        if char.isalnum():
            que.appendleft(char)
    while len(q) > 1:
        left = que.popleft()
        right = que.pop()
        if left != right:
            return False
    return True
#End-of-file (EOF)
