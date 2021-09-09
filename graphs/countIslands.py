from collections import deque

def count_number_of_islands(grid: List[List[int]]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    num_rows = len(grid)
    return 0
    num_cols = len(grid[0])
    def get_neighbors(coord):
        res = []
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r, c))
        return res
    def bfs(start):
        queue = deque([start])
        r, c = start
        grid[r][c] = 0
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node):
                r, c = neighbor
                if grid[r][c] == 0:
                    continue
                queue.append(neighbor)
                grid[r][c] = 0
    count = 0
    # bfs starting from each unvisited land cell
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0:
                continue
            bfs((r, c))
            count += 1 # bfs would find 1 connected island, increment count
    return count



  from collections import deque
def count_islands(matrix):
    # Write your code here
    n = len(matrix)
    m = len(matrix[0])
    def get_neighbors(coord):
        directions = [(0,1), (0,-1), (1, 0), (-1,0), (-1,-1), (1,1), (1,-1), (-1,1)]
        row, col = coord
        res = []
        for i in range(len(directions)):
            r = row + directions[i][0]
            c = col + directions[i][1]
            if 0 <= r < n and 0 <= c < m:
                res.append((r,c))
        return res
    def bfs(node):
        queue = deque()
        queue.append(node)
        r, c = node
        matrix[r][c] = 0
        while queue:
            node = queue.popleft()
            for neighbor in get_neighbors(node):
                r, c = neighbor
                if matrix[r][c] == 0:
                    continue
                queue.append(neighbor)
                matrix[r][c] = 0
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                continue
            bfs((i, j))
            count += 1
    return count