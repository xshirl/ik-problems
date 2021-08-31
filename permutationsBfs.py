def permutations(nums):
  result = []
  bfs(nums, 0, [], result)
  return result

def bfs(nums, index, currentPermutation, result):
  if index == len(nums):
    result.append(currentPermutation)
  else:
    for i in range(len(currentPermutation) +1):
      newPermutation = list(currentPermutation)
      newPermutation.insert(i, nums[index])
      bfs(nums, index+1, newPermutation, result)

