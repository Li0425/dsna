from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rc_color = image[sr][sc]
        m, n = len(image), len(image[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        visited = set()
        
        for d in dirs:
            i, j = sr, sc
            while 0 <= i < m and 0 <= j < n:
                if image[i][j] == rc_color:
                    image[i][j] = newColor
                    visited.add((i, j))
                    i += d[0]
                    j += d[1]
                else:
                    i += m
                    j += n
        
        print(f"visited: {visited}")

        for visited_pix in visited:
            for d in dirs:
                i, j = visited_pix[0], visited_pix[1]
                while 0 <= i < m and 0 <= j < n:
                    if image[i][j] == rc_color:
                        image[i][j] = newColor
                        i += d[0]
                        j += d[1]
                    else:
                        i += m
                        j += n

        return image

s = Solution()
result = s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)
print(result)