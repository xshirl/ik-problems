def sortArray(self, nums: List[int]) -> List[int]:
  if len(nums) < 2:
      return nums
  pivot = nums[0]
  less = [i for i in nums[1:] if i <= pivot]
  greater = [i for i in nums[1:] if i > pivot]
  return self.sortArray(less) + [pivot] + self.sortArray(greater)