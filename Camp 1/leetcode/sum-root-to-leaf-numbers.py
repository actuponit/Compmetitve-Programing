# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recur(node, n):
            if not node:
                return 0
            n = (n * 10) + node.val
            if (not node.right and not node.left):
                return n
            return recur(node.right, n) + recur(node.left, n)
        return recur(root, 0)