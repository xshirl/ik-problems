
from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        queue = deque()
        queue.append(0)
        while queue:
            node = queue.popleft()
            for child in rooms[node]:
                if not visited[child]:
                    visited[child] = True
                    queue.append(child)
        if all(visited):
            return True
        return False 
            
            