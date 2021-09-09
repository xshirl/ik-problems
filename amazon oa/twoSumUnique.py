def twoSum(nums, target):
  seen = set()
  complement = set()
  for num in nums:
    if target-num in complement:
      pair = (num, target-num) if num < target-num else (target-num, num)
      seen.add(pair)
    complement.add(num)
  return len(seen)