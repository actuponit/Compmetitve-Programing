# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def func(root, mini, maxi):
            if not root:
                return True
            if root.val < maxi and root.val > mini:
                return func(root.left, mini, root.val) and func(root.right, root.val, maxi)
            else:
                return False

        return func(root, float('-inf'), float('inf'))
        