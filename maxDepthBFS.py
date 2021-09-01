from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        queue = deque()
        queue.append(root)
        if root is None:
            return 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth