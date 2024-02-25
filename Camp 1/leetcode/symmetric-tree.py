# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(rig, lef):
            if not rig and not lef:
                return True
            if not rig or not lef:
                return False
            if rig.val == lef.val:
                t1 = mirror(rig.right, lef.left)
                t2 = mirror(rig.left, lef.right)
                return t1 and t2
            else:
                return False
        return mirror(root.right, root.left)
