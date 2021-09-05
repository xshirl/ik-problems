import heapq

def maxDistinct(nums,k):
  count = 0
  if len(nums) == k:
    return count
  freq = {}
  for i in nums:
    freq[i] = freq.get(i, 0) + 1
  minHeap = []
  for num, frequency in freq.items():
    if frequency == 1:
      count += 1
    else:
      heapq.heappush(minHeap, (frequency,num))
  while k > 0 and minHeap:
    frequency, num = heapq.heappop(minHeap)
    k -= frequency - 1
    if k >= 0:
      count += 1

  if k > 0:
    count -= k
  return count 