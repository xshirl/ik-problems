def duplicates(nums):
  freq = [0] * len(nums)
  res = []
  for i in range(len(nums)):
    freq[nums[i]-1] += 1
  # print(frequency)
  for i in range(len(freq)):
    if freq[i] > 1:
      res.append(i+1)
  return res

print(duplicates([3,3,2]))