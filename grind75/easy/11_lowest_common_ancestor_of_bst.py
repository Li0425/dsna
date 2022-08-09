from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # My solution after reading solution explanation
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     node_q = deque([root])
    #     while node_q:
    #         curr = node_q.pop()
    #         if p.val < curr.val and q.val < curr.val:
    #             node_q.append(curr.left)
    #         elif p.val > curr.val and q.val > curr.val:
    #             node_q.append(curr.right)
    #         else:
    #             return curr

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        p_val, q_val = p.val, q.val
        while node:
            node_val = node.val
            if p_val < node_val and q_val < node_val:
                node = node.left
            elif p.val > node_val and q.val > node_val:
                node = node.right
            else:
                return node

    # Recursion
    # def lowestCommonAncestor(self, root, p, q):
    #     parent_val = root.val
    #     p_val, q_val = p.val, q.val

    #     if p_val > parent_val and q_val > parent_val:    
    #         return self.lowestCommonAncestor(root.right, p, q)
    #     elif p_val < parent_val and q_val < parent_val:    
    #         return self.lowestCommonAncestor(root.left, p, q)
    #     else:
    #         return root    
