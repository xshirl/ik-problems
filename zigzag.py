from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)

  leftToRight = True

  while queue:
    levelSize = len(queue)
    currentLevel = deque()
    for _ in range(levelSize):
      currentNode = queue.popleft()
      if leftToRight:
        currentLevel.append(currentNode.val)
      else:
        currentLevel.appendleft(currentNode.val)
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
    result.append(list(currentLevel))
    leftToRight = not leftToRight

  return result

def traverse2(root):
  result = []
  queue = deque()
  queue.append(root)
  leftToRight = True
  while queue:
    size = len(queue)
    currentLevel = deque()
    for _ in range(size):
      node = queue.popleft()
      if leftToRight:
        currentLevel.append(node)
      else:
        currentLevel.appendleft(node)
    result.append(list(currentLevel))
  return result

