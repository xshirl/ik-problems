def sum(root):
  def dfs(node, sum):
    if node is None:
      return 0
    
    sum = 10 * sum + node.val

    if node.left is None and node.right is None:
      return sum
    return dfs(node.left, sum) + dfs(node.right, sum)

  return dfs(root, 0)