def dfs(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def traverse(i, j):
        if (i, j) in visited:
            return

        visited.add((i, j))

        for dir in directions:
            next_i, next_j = i+dir[0], j+dir[i]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                # Add in question-specific checks, where relevant.
                traverse(next_i, next_j)

    for i in range(rows):
        for j in range(cols):
            traverse(i, j)
