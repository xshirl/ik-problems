def find_boundary(arr):
  left, right = 0, len(arr) - 1
  index = -1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid]:
      index = mid
      right = mid - 1
    else:
      left = mid + 1
  return index

  # An array of boolean values is divided into two sections; the left section consists of all false and the right section consists of all true. Find the boundary of the right section, i.e. the index of the first true element. If there is no true element, return -1.