from collections import deque
# use double-ended queues and not python list as enqueuing is O(1), not O(n)


def bfs(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def traverse(i, j):
        queue = deque([(i, j)])
        while queue:
            curr_i, curr_j = queue.popleft()
            if (curr_i, curr_j) not in visited:
                visited.add((curr_i, curr_j))
                for dir in directions:
                    next_i, next_j = curr_i+dir[0], curr_j+dir[1]
                    if 0 <= next_i < rows and 0 <= next_j < cols:
                        # Add in question-specific checks, where relevant.
                        queue.append((next_i, next_j))

    for i in range(rows):
        for j in range(cols):
            traverse(i, j)
