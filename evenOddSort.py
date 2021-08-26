def evenOddSort(arr):
  i = 0
  j = len(arr) - 1
  while i < j:
    if arr[i] % 2 == 0:
      i += 1
    else:
      arr[i], arr[j] = arr[j], arr[i]
      j -=1
  return arr
