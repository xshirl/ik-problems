def pathSum2(root, sum):
  allPaths = []

  def dfs(node, sum, path, allPaths):
    if node is None:
      return
    path.append(node.val)
    if node.val == sum and node.left is None and node.right is None:
      allPaths.append(list(path))
    else:
      dfs(node.left, sum - node.val, path, allPaths)
      dfs(node.right, sum - node.val, path, allPaths)
    del path[-1]

  dfs(root, sum, [], allPaths)
  return allPaths