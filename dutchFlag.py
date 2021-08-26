def dutchFlag(balls):
  i = 0
  j = 0
  k = len(balls) - 1

  whiel i <= k:
  if balls[i] == 'R':
    balls[i], balls[j] = balls[j], balls[i]
    i += 1
    j += 1
  elif balls[i] == 'G':
    i += 1
  else:
    balls[i], balls[k] = balls[k], balls[i]
    k -= 1

  