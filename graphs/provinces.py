class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        count = 0
        def dfs(isConnected, visited, i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(isConnected, visited, j)
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(isConnected, visited, i)
                count += 1
                
        return count