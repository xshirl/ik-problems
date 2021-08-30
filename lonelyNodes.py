class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root):
            if root:
                dfs(root.left)
                if root.left and root.right is None:
                    res.append(root.left.val)
                if root.right and root.left is None:
                    res.append(root.right.val)
                dfs(root.right)
        dfs(root)
        return res