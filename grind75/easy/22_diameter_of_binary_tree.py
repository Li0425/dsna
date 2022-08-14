from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # my solution that passed
    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        q = deque([root])
        while q:
            curr = q.popleft()
            left_path = right_path = 0
            if curr.left:
                q.append(curr.left)
                left_path = self.get_height(curr.left)
            if curr.right:
                q.append(curr.right)
                right_path = self.get_height(curr.right)
            diameter = max(left_path + right_path, diameter)
        return diameter

    # provided
    # def diameterOfBinaryTree(self, root: TreeNode) -> int:
    #     diameter = 0

    #     def longest_path(node):
    #         if not node:
    #             return 0
    #
    #         nonlocal diameter

    #         left_path = longest_path(node.left)
    #         right_path = longest_path(node.right)

    #         diameter = max(diameter, left_path + right_path)

    #         # return the longest one between left_path and right_path;
    #         # add 1 for the path connecting the node and its parent
    #         return max(left_path, right_path) + 1

    #     longest_path(root)
    #     return diameter