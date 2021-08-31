def find_diameter(root):
  treeDiameter = 0
  def height(node):
    if node is None:
      return 0
    leftTree = height(node.left)
    rightTree = height(node.right)

    if leftTree and rightTree:
      diameter = leftTree + rightTree + 1
      treeDiameter = max(treeDiameter, diameter)

    return max(leftTree, rightTree)  + 1

  height(root)
  return treeDiameter
  
  