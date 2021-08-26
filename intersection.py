def intersection(arr1, arr2, arr3):

  def find(a,b):
    i = 0
    j = 0
    output = []

    while i < len(a) and j < len(b):
      if a[i] > b[j]:
        j += 1
      elif a[i] < b[j]:
        i += 1
      else:
        output.append(a[i])
        i += 1
        j += 1
    return output

    
  res = intersection(arr1, arr2)
  final = intersection(res, arr3)

  if len(final) == 0:
    return [-1]
  return final

  
