# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traversal(node, row, col):
            if not node:
                return
            mp[col].append([row, node.val])
            traversal(node.left, row+1, col-1)
            traversal(node.right, row+1, col+1)
        mp = defaultdict(list)
        traversal(root, 0, 0)
        print(mp)
        arr = [0] * len(mp)
        offset = abs(min(mp.keys()))
        for i in mp:
            mp[i].sort()
            arr[offset+i] = list(map(lambda x: x[1], mp[i]))
        return arr
        