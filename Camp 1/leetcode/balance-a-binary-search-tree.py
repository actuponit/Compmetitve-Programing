# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        arr = []
        inorder(root)
        print(arr)
        def toBST(l, r):
            if l > r:
                return None
            # if l == r:
            #     return TreeNode(arr[l])
            mid = (l+r) // 2
            node = TreeNode(arr[mid])
            node.left = toBST(l, mid-1)
            node.right = toBST(mid+1, r)
            return node 
        return toBST(0, len(arr)-1)
        