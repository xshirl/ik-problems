from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        nodes = {}
        for i in range(len(graph)):
            nodes[i] = graph[i]
        res = []
        print(nodes)
        def bfs(graph, start, end):
            visited = [False] * len(graph)
            queue = deque()
            queue.append((0, []))
            path = []
            while queue:
                node, path = queue.popleft()
                if node == end:
                    res.append((path + [node]))
                for child in graph[node]:
                    queue.append((child, path+[node]))
            return res
        return bfs(graph, 0, len(graph) - 1)