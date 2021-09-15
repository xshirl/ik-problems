import heapq
def kth_largest_in_an_array(numbers, k):
    heapq.heapify(numbers)
    for i in range(len(numbers) - k):
        heapq.heappop(numbers)
    return heapq.heappop(numbers)