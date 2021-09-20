class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n
        for i, j in edges:
            indegrees[j] += 1
        ans = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                ans.append(i)
        return ans