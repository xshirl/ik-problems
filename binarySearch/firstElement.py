# Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.
def firstElement(arr, target):
  index = -1
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] < target:
      left = mid + 1
    else:
      index = mid
      right = mid - 1
  return index


  