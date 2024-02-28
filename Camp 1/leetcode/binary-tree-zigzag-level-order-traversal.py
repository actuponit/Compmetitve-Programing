# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)
        def traverse(node, level):            
            if not node:
                return
            
            mp[level].append(node.val)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)


        traverse(root, 0)
        arr = [0] * len(mp)
        for i, j in mp.items():
            if i % 2 == 1:
                print(j)
                j.reverse()
                
            arr[i] = j
        return arr
        