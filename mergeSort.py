def merge_sort(arr):
  mergeSortHelper(arr, 0, len(arr) -1)
  return arr

def mergeSortHelper(arr, start, end):
  if start >= end:
    return
  mid = (start + end) // 2
  mergeSortHelper(arr, start, mid)
  mergeSortHelper(arr, mid + 1, end)

  i = start
  j = mid + 1
  result = []

  while i <= mid and j <= end:
    if arr[i]< arr[j]:
      result.append(arr[i])
      i += 1
    else:
      result.append(arr[j])
      j += 1

  while i <= mid:
    result.append(arr[i])
    i += 1
  while j <= end:
    result.append(arr[j])
    j += 1
  

  arr[start: end + 1] = result

  return arr