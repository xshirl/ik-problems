from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        directions = [(0, 1), (1,0), (0, -1), (-1, 0)]
        queue = deque()
        n = len(rooms)
        m = len(rooms[0])
        for i, row in enumerate(rooms):
            for j, entry in enumerate(row):
                if entry == 0:
                    queue.append((i, j))
        while queue:
            row, col = queue.popleft()
            for x, y in directions:
                total_row, total_col = row + x, col + y
                if 0 <= total_row < n and 0 <= total_col < m:
                    if rooms[total_row][total_col] == 2147483647:
                        rooms[total_row][total_col] = rooms[row][col] + 1
                        queue.append((total_row, total_col))
        return rooms
