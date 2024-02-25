# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def mode(node, mp):
            
            if not node:
                return
            mp[node.val] = mp.get(node.val, 0) + 1
            mode(node.left, mp)
            mode(node.right, mp)
            return mp
        mp = mode(root, {})
        maxi = max(mp.values()) 
        ans = []
        for i, j in mp.items():
            if j == maxi:
                ans.append(i)
        return ans 

        