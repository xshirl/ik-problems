import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for point in points:
            heapq.heappush(heap, ((math.sqrt(point[0] ** 2 + point[1]**2)), point))
        for i in range(k):
            diff, point = heapq.heappop(heap)
            res.append(point)
        return res