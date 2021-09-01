def inorder(root):
  stack = []
  curr = root
  res = []
  while stack or curr:
    if curr:
      stack.append(curr)
      curr = curr.left

    else:
      curr = stack.pop()
      res.append(curr.val)
      curr = curr.right
  return res

def preorder(root):
  if not root:
    return []
  res = []
  stack = [root]
  while stack:
    top = stack.pop()
    res.append(top.val)
    if top.right:
      stack.append(top.right)
    if top.left:
      stack.append(top.left)
  return res


def postorder(root):
  res = []
  stack = []
  prev = None
  p = root
  while stack or p:
    if p:
      stack.append(p)
      p = p.left
    else:
      top = stack[-1]
      if top.right and top.right != prev:
        p = top.right
      else:
        res.append(top.val)
        prev = top
        stack.pop()
  return res

  
