from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_height(self, node):
        if not node:
            return 0
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    # My initial wrong solution: only balanced at root, not at every node
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if not root or (not root.left and not root.right):
    #         return True

    #     if root.left and root.right:
    #         return abs(self.get_height(root.left)-self.get_height(root.right)) <= 1
        
    #     if not root.left or not root.right:
    #         return self.get_height(root.left) == 1 or self.get_height(root.right) == 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return abs(self.get_height(root.left)-self.get_height(root.right)) <= 1 \
            and self.isBalanced(root.left) \
                and self.isBalanced(root.right)
