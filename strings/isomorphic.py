def isomorphicStrings(s1, s2):
  hashmap = {}
  used = set()
  if len(s1) != len(s2):
    return False
  for i in range(len(s1)):
    a = s1[i]
    b = s2[i]
    if a in hashmap:
      if hashmap[a] != b:
        return False
    else:
      if b in used:
        hashmap[a] = b
        used.add(b)
  return True