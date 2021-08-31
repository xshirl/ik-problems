from heapq import * 


def kSmallest(nums, k):
  maxHeap = []
  for i  in range(k):
    heappush(maxHeap, -nums[i])

  for i in range(k, len(nums)):
    if -nums[i] > maxHeap[0]:
      heappop(maxHeap)
      heappush(maxHeap, -nums[i])

  return -maxHeap[0]
  