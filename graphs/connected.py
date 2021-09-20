from collections import deque
from collections import defaultdict
def number_of_connected_components(n, edges):
    # Write your code here
    
    graph = defaultdict(lambda:[])
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
        
    visited = [False] * n
    
    def bfs(node):
        queue = deque()
        queue.append(node)
        while queue:
            visited[node] = True
            node = queue.popleft()
            for child in graph[node]:
                if not visited[child]:
                    visited[child] = True
                    queue.append(child)
    total = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            total += 1
    return total