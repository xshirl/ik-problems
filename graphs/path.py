from collections import deque
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        def return_graph(edges):
            graph = defaultdict(lambda:[])
            for i, j in edges:
                graph[i].append(j)
                graph[j].append(i)
            return graph
        def bfs(graph, start, end):
            
            visited = set()
            queue = deque()
            queue.append(start)
            while queue:
                out = queue.popleft()
                if end == out:
                    return True
                for node in graph[out]:
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)
            return False 
        if not edges:
            return True
        graph = return_graph(edges)
        return bfs(graph, start, end)