class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def count_paths(root, S):
  def dfs(node, S, currentPath):
    if currentNode is None:
      return 0

    currentNode.append(currentNode.val)
    pathCount, pathSum = 0, 0

    for i in range(len(currentPath-1), -1, -1):
      pathSum += currentPath[i]
      if pathSum == S:
        pathCount += 1

    pathCount += dfs(node,left, S, currentPath)
    pathCount += dfs(node.right, S, currentPath)

    del currentPath[-1]
    return pathCount

    
  
  return dfs(root, S, [])
