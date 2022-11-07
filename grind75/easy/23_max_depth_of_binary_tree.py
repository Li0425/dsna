from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my recursion solution:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 1 # was confused over here, tried 0 at the beginning
        if root.left or root.right:
            max_depth = max(self.maxDepth(root.left),
                            self.maxDepth(root.right)) + 1
        return max_depth


# official solution: TC: O(N), SC: O(N) worst case, O(logN) avg case
# recursion call will occur (height of tree) times
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

# official iteration solution:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(1, root)] if root else []
        
        depth = 0
        while stack:
            curr_depth, root = stack.pop()
            if root:
                depth = max(depth, curr_depth)
                stack.append((curr_depth+1, root.left))
                stack.append((curr_depth+1, root.right))

        return depth
                