from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        visited = set()
        direc = ((0, -1), (0, 1), (-1, 0), (1, 0))
        original_color = image[sr][sc]
        
        q = deque([(sr, sc)])
        while q:
            curr = q.popleft()
            if curr not in visited:
                visited.add(curr)
                if image[curr[0]][curr[1]] == original_color:
                    image[curr[0]][curr[1]] = color
                    for d in direc:
                        if 0 <= curr[0]+d[0] < m and 0 <= curr[1] + d[1] < n:
                            neighbour = (curr[0]+d[0], curr[1]+d[1])
                            q.append(neighbour)
        
        return image
        