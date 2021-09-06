# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res = []
        res2 = []
        def dfs(root):
            res = []
            if not root:
                return res
            if root:
                if root.left is None and root.right is None:
                    return [root.val]
            return dfs(root.left) + dfs(root.right)
        return dfs(root1) == dfs(root2)
                    