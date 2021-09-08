from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])
        fresh_oranges = 0
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        queue.append((-1, -1))
        minutes = -1
        while queue:
            row, col = queue.popleft()
            if row == -1:
                minutes += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for d in directions:
                    n_row, n_col = row + d[0], col + d[1]
                    if 0<= n_row<n and 0<=n_col<m:
                        if grid[n_row][n_col] == 1:
                            grid[n_row][n_col] = 2
                            fresh_oranges -= 1
                            queue.append((n_row, n_col))
        return minutes if fresh_oranges == 0 else -1