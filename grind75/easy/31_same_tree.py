from typing import Optional


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # Iterative
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     def check(p, q):
    #         if not p and not q:
    #             return True
    #         if not p or not q:
    #             return False
    #         if p.val != q.val:
    #             return False
    #         return True
            
    #     queue = deque([(p, q)])
    #     while queue:
    #         curr_p, curr_q = queue.popleft()
    #         if not check(curr_p, curr_q):
    #             return False
    #         if curr_p:
    #             queue.append((curr_p.left, curr_q.left))
    #             queue.append((curr_p.right, curr_q.right))
    #     return True
