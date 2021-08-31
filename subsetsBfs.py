def find_subsets(nums):
  subsets = []
  subsets.append([])
  for num in nums:
    n = len(subsets)
    for i in range(n):
      set1 = list(subsets[i])
      set1.append(num)
      subsets.append(set1)
  return subsets 
  