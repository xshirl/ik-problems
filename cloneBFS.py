# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = deque()
        queue.append([original, cloned])
        while queue:
            node1, node2 = queue.popleft()
            if node1 == target:
                return node2
            if node1.left:
                queue.append([node1.left, node2.left])
            if node2.right:
                queue.append([node1.right, node2.right])
        return None
            
        
        