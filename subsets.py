def subsets(self, nums: List[int]) -> List[List[int]]:
  result = []
  def helper(S, i, slate):
      if i == len(S):
          result.append(slate[:])
      else:
          helper(S, i+1, slate)
          slate.append(S[i])
          helper(S, i+1, slate)
          slate.pop()
  helper(nums, 0, [])
  return result