# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def maxdiff(node, mini, maxi):
            if not node:
                return
            mini = min(node.val, mini)
            maxi = max(node.val, maxi)
            # print(mini, maxi)
            self.ans = max(self.ans, maxi-mini)
            maxdiff(node.left, mini, maxi)
            maxdiff(node.right, mini, maxi)
        maxdiff(root, float('inf'), -1)
        return self.ans