from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def get_neighbors(coord):
            res = []
            row, col = coord
            delta_row = [-2, -2, -1, 1, 2, 2, 1, -1]
            delta_col = [-1, 1, 2, 2, 1, -1, -2, -2]
            for i in range(len(delta_row)):
                r = row + delta_row[i]
                c = col + delta_col[i]
                res.append((r, c))
            return res
        def bfs(root):
            queue = deque([root])
            steps = 0
            visited = set()
            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    if node[0] == y and node[1] == x:
                        return steps
                    for neighbor in get_neighbors(node):
                        if neighbor in visited:
                            continue
                        queue.append(neighbor)
                        visited.add(neighbor)
                steps += 1
        return bfs((0,0))