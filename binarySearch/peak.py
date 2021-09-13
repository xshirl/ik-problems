def peak(arr):
  index = -1
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]:
      index = mid
      right = mid - 1 # get rid of all elements right of arr[mid]
    else:
      left = mid + 1 # get rid of all elements left of arr[mid] if arr[mid] < arr[mid + 1]
  return index