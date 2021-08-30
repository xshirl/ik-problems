class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.sum = 0
        def dfs(root):
            if root:
                if low <= root.val <= high:
                    self.sum += root.val
                if low < root.val:
                    dfs(root.left)
                if root.val < high:
                    dfs(root.right)
        dfs(root)
        return self.sum