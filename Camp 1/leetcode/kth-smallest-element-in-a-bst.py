# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = -1
        def traverse(node):
            if not node:
                return
            if self.k <= 0:
                return
            traverse(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            traverse(node.right)
        traverse(root)
        return self.ans
        