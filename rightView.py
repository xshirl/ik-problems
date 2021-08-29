from collections import deque

def right_view(root):
  result = []
  if root is None:
    return result
  queue = deque()
  queue.append(root)
  while queue:
    level = len(queue)
    for i in range(0, levelSize):
      node = queue.popleft()
      if i == levelSize - 1:
        result.append(node)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
  return result 