import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binary_search(row):
            low, high = 0, len(row)
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 0:
                    high = mid
                else:
                    low = mid + 1
            return low + 1
        res = []
        for i in range(len(mat)):
            strength = binary_search(mat[i])
            res.append([strength, i])
        heapq.heapify(res)
        return [heapq.heappop(res)[1] for _ in range(k)]
            