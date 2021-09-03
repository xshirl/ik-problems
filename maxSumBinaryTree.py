# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        level = 1
        res = []
        queue.append(root)
        maxSum = float(-inf)
        while queue:
            size = len(queue)
            levelSum = 0
            level = []
            for _ in range(size):
                node = queue.popleft()
                levelSum += node.val
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if levelSum > maxSum:
                maxSum = levelSum
            res.append([levelSum, level])

        for i in range(len(res)):
            if res[i][0] == maxSum:
                return i+1
