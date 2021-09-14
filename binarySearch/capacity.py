def capacity(weights, d):
  def feasible(wegihts, max_weight, d):
    days = 1
    capacity = max_weight
    i = 0
    n = len(weights)
    while i < n:
      if weights[i] <= capacity:
        capacity -= weights[i]
        i += 1
      else:
        days += 1
        capacity = max_weight
    return days <= d

  left  = max(weights)
  right = sum(weights)
  index = right
  while left <= right:
    mid = (left + right) // 2
    if feasible(weights, mid, d):
      index = mid
      right = mid - 1
    else:
      left = mid + 1
  return index