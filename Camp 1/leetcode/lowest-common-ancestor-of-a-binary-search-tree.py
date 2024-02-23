# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if q.val < p.val:
        #     q, p = p, q
        
        def find(node, p, q):
            if node.val > p.val and node.val > q.val:
                return find(node.left, p, q)
            if node.val < p.val and node.val < q.val:
                return find(node.right, p, q)
            else:
                return node
        return find(root, p, q)
        

        
        