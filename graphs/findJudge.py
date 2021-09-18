from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(lambda:[])
        count = 0
        found = set()
        visited = set()
        if n == 1:
            return 1
        for i, j in trust:
            graph[j].append(i)
            visited.add(i)
        for i, j in trust:
            if j not in visited and j not in found:
                found.add(j)
        for key, value in graph.items():
            if len(value) == n - 1 and len(found) == 1:
                return key
                
        return -1