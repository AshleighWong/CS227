"""
Name: Ashleigh Wong
Email: ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of BST.
"""

# Definition for a binary tree node.
class TreeNode:
    """Class representing a node in a binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root: TreeNode, val: int) -> TreeNode:
    """Insert a value into the Binary Search Tree (BST).
    """
    if not root:
        return TreeNode(val)
    if root.val > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
