def get_permutations(nums):
    # Write your code here
    def backtrack(first=0):
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first+1)
            nums[first], nums[i] = nums[i], nums[first]
    n = len(nums)
    output = []
    backtrack()
    return output