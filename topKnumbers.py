from heapq import *

def kLargest(nums, k):
  minHeap = []
  for i in range(k):
    heappush(minHeap, nums[i])
  
  for i in range(k, len(nums)):
    if nums[i] > minHeap[0]:
      heappop(minHeap)
      heappush(minHeap, nums[i])
  return list(minHeap)

