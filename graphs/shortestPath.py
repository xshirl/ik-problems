from collections import deque
def shortestPath(graph, a, b):
  def get_neighbors(node):
    return graph[node]
  def bfs(root,target):
    queue = deque()
    queue.append(root)
    visited = set()
    level = 0
    while queue:
      size = len(queue)
      for _ in len(size):
        node = queue.popleft()
        if node == target:
          return level
        for neighbor in get_neighbors(node):
          if neighbor in visited:
            continue
          queue.append(neighbor)
          visited.add(neighbor)
        level += 1
      return bfs(a, b)
    