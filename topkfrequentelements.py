import heapq
def find_top_k_frequent_elements(arr, k):
    """
    Args:
     arr(list_int32)
     k(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    map = {}
    for i in range(len(arr)):
        map[arr[i]] = map.get(arr[i], 0) + 1
    return heapq.nlargest(k, map.keys(), map.get)