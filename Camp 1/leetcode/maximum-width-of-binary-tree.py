# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mp = defaultdict(list)
        def traverse(node, level, k):
            if not node:
                # self.mp[level][1] += 1
                return
            # self.mp[level][0] += 1
            
            # if self.mp[level][1] > 0:
            #     self.mp[level][0] += self.mp[level][1]
            #     self.mp[level][1] = 0
            self.mp[k].append(level)
            traverse(node.left, (2*level) + 1, k+1)
            traverse(node.right, (2*level) + 2, k+1)
        traverse(root, 0, 0)
        m = 0
        for i in self.mp.values():
            m = max(i[-1] - i[0] + 1, m)
        return m