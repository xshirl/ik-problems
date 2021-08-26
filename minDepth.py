def minDepth(root):
  if root is None:
    return 0
  queue = deque()
  queue.append(root)
  minTreeDepth = 0
  while queue:
    minTreeDepth += 1
    levelSize = len(queue)
    for _ in range(levelSize):
      currentNode = queue.popleft()
      if not currentNode.left and not currentNode.right:
        return minTreeDepth
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    