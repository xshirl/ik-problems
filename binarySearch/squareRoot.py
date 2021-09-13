def squareRoot(n):
  index = -1
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if mid * mid <= n:
      index = mid
      left = mid + 1
    else:
      right = mid - 1

  return index