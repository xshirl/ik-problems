def find_path(root, sequence):
  if not root:
    return len(sequence) == 0

  def dfs(node, sequence, index):
    if node is None:
      return False
    seq = len(sequence)
    if index >= seq or node.val != seq[index]:
      return False
    if node.left is None and node.right is None and index == seq - 1:
      return True

    return dfs(node.left, seq, index+1) or dfs(node.right, seq, index+1)
  return dfs(root, sequence, 0)
  