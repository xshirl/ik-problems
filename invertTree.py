from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:  
        queue = deque()
        queue.append(root)
        if root is None:
            return root
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root