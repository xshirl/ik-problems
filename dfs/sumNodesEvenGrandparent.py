# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent, grandparent):
            if not node:
                return 0
            add = 0
            if grandparent and grandparent.val % 2 == 0:
                add += node.val
            return add + dfs(node.left, node, parent) + dfs(node.right, node, parent)
        
        return dfs(root, None, None)