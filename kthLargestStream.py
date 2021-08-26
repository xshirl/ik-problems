import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]



import heapq
def kth_largest(k, initial_stream, append_stream):
    # Write your code here
    heapq.heapify(initial_stream)
    while len(initial_stream) > k:
        heapq.heappop(initial_stream)
        
    result = []
    
    for num in append_stream:
        if len(initial_stream) < k:
            heapq.heappush(initial_stream, num)
        elif num > initial_stream[0]:
            heapq.heappushpop(initial_stream, num)
        result.append(initial_stream[0])
    
    return result