# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dvideconqure(arr):
            if not arr:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            m = max(arr)
            mid = arr.index(m)
            node = TreeNode(m)
            node.left = dvideconqure(arr[:mid])
            node.right = dvideconqure(arr[mid+1:])
            return node
            
        return dvideconqure(nums)
        