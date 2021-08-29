from collections import deque

def find_successor(root, key):
  if root is None:
    return None

  queue = deque()
  queue.append(root)

  while queue:
    node = queue.popleft()
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
    if node.val == key:
      break
  return queue[0] if queue else None


  