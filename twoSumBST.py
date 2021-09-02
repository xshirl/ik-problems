# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nums = set()
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if k - node.val in nums:
                    return True
                else:
                    nums.add(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False