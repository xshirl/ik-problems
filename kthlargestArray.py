import heapq
def kth_largest_in_an_array(numbers, k):
    return heapq.nlargest(k, numbers)[-1]