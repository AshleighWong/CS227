"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""
from typing import Optional

class ListNode:
    """Class representing node for list"""
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node
def increment_num(lst: Optional['ListNode']) -> Optional['ListNode']:
    """Function that increments list by 1 and takes into account carry"""
    if not lst:
        return ListNode(1)
    carry = 1
    head = lst
    prev = None
    while lst and carry:
        lst.val += carry
        if lst.val == 10:
            lst.val = 0
            carry = 1
        else:
            carry = 0
        prev = lst
        lst = lst.next
    if carry:
        prev.next = ListNode(1)
    return head
#End-of-file (EOF)
