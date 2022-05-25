from collections import deque
from typing import List


class Solution:
    
# My wrong solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = set()
        
        # q as the queue of cells to be examined next
        queue = deque([])
        
        # add all coordinates of cells with 0 to q
        dist = mat.copy()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    dist[i][j] = 10 ** 4 * 2
                    
        while queue:
            curr_i, curr_j = queue.popleft()
            for direc in directions:
                next_i, next_j = curr_i+direc[0], curr_j+direc[1]
                if (next_i, next_j) not in visited:
                    if 0 <= next_i < rows and 0 <= next_j < cols:
                        if mat[next_i][next_j] <= dist[next_i][next_j]:
                            dist[next_i][next_j] = dist[curr_i][curr_j] + 1
                            queue.append((next_i, next_j))

        return dist


# s = Solution()
# ans = s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
# print(ans)