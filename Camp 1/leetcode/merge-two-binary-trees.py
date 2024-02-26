# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root1 and not root2:
        #     return None
        if not root1 and not root2:
            return None
        newRoot = TreeNode()
        curr = newRoot
        def merge(root1, root2, curr, d = ''):
            if not root1 and not root2:
                return None
            val1 = root1.val if root1 else 0
            val2 = root2.val if root2 else 0
            
            if d == 'left':
                curr.left = TreeNode(val1 + val2)
                curr = curr.left
            elif d == 'right':
                curr.right = TreeNode(val1 + val2)
                curr = curr.right
            else:
                curr.val = val1 + val2
            
            left1 = root1.left if root1 else None 
            left2 = root2.left if root2 else None 
            right1 = root1.right if root1 else None 
            right2 = root2.right if root2 else None 
            merge(left1, left2, curr, 'left')
            merge(right1, right2, curr, 'right')
        merge(root1,root2,curr)
        return newRoot
            
        