class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def pathSum(root, sum):
  if root is None:
    return False

  if root.val == sum and root.left is None and root.right is None:
    return True

  return pathSum(root.left, sum - root.val) or pathSum(root.right, sum-root.val)


