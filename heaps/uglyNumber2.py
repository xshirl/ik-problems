import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        used = {1}
        factors = [2,3,5]
        for i in range(n-1):
            val = heapq.heappop(ans)
            for multiplier in factors:
                if val * multiplier not in used:
                    heapq.heappush(ans, val*multiplier)
                    used.add(val*multiplier)
        return ans[0]