class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        maxCount = 0
        res = []
        for edge in edges:
            res.append(edge[0])
            res.append(edge[1])
        for num in res:
            maxCount = max(maxCount, res.count(num))
            if res.count(num) == n:
                return num
            