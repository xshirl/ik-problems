def preorder(root):
  stack = []
  res = []
  if not root:
      return res
  stack.append(root)
  while stack:
      node = stack.pop()
      res.append(node.val)
      if node.right:
          stack.append(node.right)
      if node.left:
          stack.append(node.left)
  return res