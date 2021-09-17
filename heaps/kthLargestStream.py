import heapq

def kth_largest(k, initial_stream, append_stream):
    # Write your code here
    heap = initial_stream
    heapq.heapify(heap)
    res = []
    while len(heap) > k:
        heapq.heappop(heap)
    for i in range(len(append_stream)):
        val = append_stream[i]
        if len(heap) < k:
            heapq.heappush(heap, val)
        elif val > heap[0]:
            heapq.heappushpop(heap, val)
        res.append(heap[0])
    return res