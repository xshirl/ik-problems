class TreeNode:
  def __init__(self, val):
    self.val = val
    self.children = []

from collections import deque

def levelOrder(root):
  res = []
  queue = deque()
  queue.append(root)
  while queue:
    size = len(queue)
    level  =  []
    for _ in range(size):
      node = queue.popleft()
      level.append(node)
      for child in node.children:
        queue.append(child)
    res.append(level)
  return res 