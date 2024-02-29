# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def recur(st, en):
            
            if st > en:
                return None
            mid = (st+en) // 2
            root = TreeNode(nums[mid])
            root.left = recur(st, mid-1)
            root.right = recur(mid+1, en)
            return root
        return recur(0, len(nums) - 1)