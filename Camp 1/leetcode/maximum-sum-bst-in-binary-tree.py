# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBST(self, node):
        if not node:
            return (0, float('-inf'), float('inf'))
        if not node.left and not node.right:
            self.maxsum = max(self.maxsum, node.val)
            return (node.val, node.val, node.val)
        
        l = self.isBST(node.left)
        r = self.isBST(node.right)
        if l[1] < node.val and r[2] > node.val:
            s = node.val + l[0] + r[0]
            self.maxsum = max(self.maxsum, s)
            return (s, max(node.val, r[1]), min(node.val, l[2]))
        else:
            return (0, float('inf'), float('-inf'))

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxsum = 0
        self.isBST(root)
        return self.maxsum
        