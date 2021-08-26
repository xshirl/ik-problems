from collections import deque

class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left, self.right = None, None

def levelAverages(root):
  result = []
  queue = deque()
  if root is None:
    return result

  queue.append(root)
  while queue:
    levelSize = len(queue)
    levelSum = 0.0
    for _ in range(levelSize):
      currentNode = queue.popleft()
      levelSum += currentNode.val
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

      result.append(levelSum/levelSize)
  return result

def levelSum(root):
  result = []
  queue = deque()
  queue.append(root)
  while queue:
    size = len(queue)
    levelSum = 0.0
    for _ in range(size):
      node = queue.popleft()
      levelSum += node.val
      if node.left:
        queue.append(currentNode.left)
      if node.right:
        queue.append(currentNode.right)
  return result 
