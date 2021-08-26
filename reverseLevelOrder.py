from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  queue = deque()
  queue.append(root)

  while queue:
    size = len(queue)
    currentLevel = []
    for _ in range(size):
      node = queue.popleft()
      currentLevel.append(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    result.appendleft(currentLevel)

  return result

  
      