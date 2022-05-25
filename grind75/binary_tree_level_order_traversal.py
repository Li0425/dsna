from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        dic = {} # level: [nodes]
        
        # traverse the tree in breath-first manner
        # update dic as exploration is on-going
        level_counter = 0
        visited = set()
        q = deque([root])
        while q:
            curr_node = q.popleft()
            if curr_node not in visited:
                visited.add(curr_node)
                if dic.get(level_counter) is None:
                    dic[level_counter] = [curr_node]
                else:
                    dic[level_counter].append(curr_node)
                    
                next_level = level_counter + 1
                
                left_child = curr_node.left
                if left_child:
                    if dic.get(next_level) is None:
                        dic[next_level] = [left_child]
                    else:
                        dic[next_level] = dic[next_level].append(left_child)
                    q.append(left_child)
                
                right_child = curr_node.right
                if right_child:
                    if dic.get(next_level) is None:
                        dic[next_level] = [right_child]
                    else:
                        dic[next_level] = dic[next_level].append(right_child)
                    q.append(right_child)
                
                level_counter += 1
        
        ans = []
        for _, v in dic.items():
            l = []
            for node in v:
                l.append(node.val)
            ans.append(l)
        
        return ans