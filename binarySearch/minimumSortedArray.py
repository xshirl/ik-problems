def minRotated(arr):
  index = -1
  left, right = 0, len(arr) - 1
  last = arr[-1]
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] > last:
      left = mid + 1
    else:
      index = mid
      right = mid - 1
  return index
  