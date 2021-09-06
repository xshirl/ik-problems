def find_target(root, target):
  if root is None:
    return None
  if root.val == target:
    return root
  return find_target(root.left, target) or find_target(root.right, target)