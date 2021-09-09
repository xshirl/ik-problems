def topoSort(graph):
  visited = {}
  stack = []
  def dfs(node):
    if node in visited:
      if visited[node]:
        return
    visited[node] = False
    for child in graph[node]:
      dfs(child)
    visited[node] = True
    stack.append(node)
  for node in graph.keys():
    dfs(node)
  return stack[::-1]