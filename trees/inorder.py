def inorder(root):
  curr = root
  stack = []
  res = []

  while curr or stack:
    while curr:
      stack.append(curr)
      curr = curr.left
    curr = stack.pop()
    res.append(curr.val)
    curr = curr.right
  return res