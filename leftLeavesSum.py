# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        leftSum = 0
        queue = deque()
        queue.append([root, False])
        while queue:
            size = len(queue)
            for _ in range(size):
                node, left = queue.popleft()
                if node.left:
                    queue.append([node.left, True])
                if node.right:
                    queue.append([node.right, False])
                if not node.left and not node.right:
                    if left:
                        leftSum += node.val
                        
        return leftSum