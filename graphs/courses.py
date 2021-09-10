def can_be_completed(n, a, b):
    graph = [[] for _ in range(n)]
    for i in range(len(a)):
        graph[a[i]].append(b[i])
    
    
    visited = [0 for _ in range(n)]
    

    def dfs(graph, u, visited):
        visited[u] = 1
        
        for v in graph[u]:
            if visited[v] == 0:
                if not dfs(graph, v, visited):
                    return False
            elif visited[v] == 1:
                return False
        visited[u] = 2
        return True 

    for i in range(n):
        if visited[i] == 0:
            if not dfs(graph, i, visited):
                return False
    return True
    