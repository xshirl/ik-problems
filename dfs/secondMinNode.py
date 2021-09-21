# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def inorder(root, res):
            if root:
                if root.left:
                    inorder(root.left, res)
                res.append(root.val)
                if root.right:
                    inorder(root.right, res)
        res = []
        inorder(root, res)
        minValue = -1
        res.sort()
        for i in range(len(res)):
            if res[i] != res[0] and res[i] > minValue:
                minValue = res[i]
                break
        return minValue
            