def insert(root, val:
  if root is None:
    return Node(val)
  if root.val < val:
    root.right = insert(root.right, val)
  elif root.val > val:
    root.left = insert(root.left, val)
  return root