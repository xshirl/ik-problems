import heapq

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         return heapq.nlargest(k, nums)[-1]

def kthElement(nums):
  heapq.heapify(nums)
  print(nums)
  return nums

print(kthElement([5,3,7]))