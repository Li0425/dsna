from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Iterative: swap left and right child of all notes in the tree
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        # queue to store nodes whose left & right children have not been swapped
        q = deque([root])
        while q:
            curr = q.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.right:
                q.append(curr.right)
            if curr.left:
                q.append(curr.left)
        return root
    
    # Recursive:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return
        
    #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #     return root