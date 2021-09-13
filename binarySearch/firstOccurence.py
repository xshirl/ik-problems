# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. Return -1 if the target is not in the array.

def firstOccurence(arr, target):
  index = -1
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      index = mid
      right = mid - 1
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return index 