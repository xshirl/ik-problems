def subsets(s):
  res = []
  def helper(slate, i):
    if i == len(s):
      res.append(slate)
    else:
      helper(slate, i+1)
      helper(slate + s[i], i+1)
  helper("", 0)
  return res