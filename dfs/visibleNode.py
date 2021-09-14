def visibleNode(root):
  def dfs(root, maxValue):
    if not root:
      return 0
    total = 0
    if root.val >= maxValue:
      total += 1

    total += dfs(root.left, max(maxValue, root.val))
    total += dfs(root.right, max(maxValue, root.val))
    return total
  return dfs(root, -float(inf))

#runtime O(n) (O(2n-1))