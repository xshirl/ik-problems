from collections import deque
def max_island_size(grid):
    """
    Args:
        grid (List[List[int]])
    Returns:
        int
    """
    # Write your code here
    n = len(grid)
    m = len(grid[0])
    def get_neighbors(coord):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        row, col = coord
        res = []
        for i in range(len(directions)):
            n_row = row + directions[i][0]
            n_col = col + directions[i][1]
            if 0 <= n_row < n and 0 <= n_col < m:
                res.append((n_row, n_col))
        return res
        
    def bfs(root):
        queue = deque()
        queue.append(root)
        r, c = root
        grid[r][c] = 0
        oneCount = 1
        while queue:
            node = queue.popleft()
            for neighbor in get_neighbors(node):
                r, c = neighbor
                if grid[r][c] == 1:
                    oneCount += 1
                    queue.append(neighbor)
                    grid[r][c] = 0
        return oneCount
        
    maxCount = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue
            maxCount = max(maxCount, bfs((i,j)))
    return maxCount