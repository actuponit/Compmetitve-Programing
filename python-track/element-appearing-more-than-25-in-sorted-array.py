class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        fourth = len(arr)*0.25
        mp = {}
        for i in arr:
            mp[i] = mp.get(i, 0) + 1
            if mp[i] > fourth:
                return i
        
"""
9 * 25 / 100

"""