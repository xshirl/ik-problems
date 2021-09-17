def postorderStack(root):
  stack = []
  res = []
  stack.append(root)
  if root is None:
      return res
  while stack:
      node = stack.pop()
      res.append(node.val)
      if node.left:
          stack.append(node.left)
      if node.right:
          stack.append(node.right)
  return res[::-1]


  # left right root
  # root right left 
  