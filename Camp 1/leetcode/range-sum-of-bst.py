# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # add all numbers greater than 5
        
        def greater(node, val):
            if not node:
                return 0
            ans = 0
            if node.val > val:
                ans = node.val
                ans += greater(node.left, val)
                ans += greater(node.right, val)
            elif node.val <= val:
                if node.val == val: 
                    ans = node.val

                ans += greater(node.right, val)
            return ans
        return greater(root, low) - greater(root, high) + high 
        