class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        maps = {}
        count = 0
        for i in nums:
            maps[k-i] = 0
        for i in nums:
            if i in maps and maps[i] > 0:
                maps[i] -= 1
                count += 1
            
            else:
                maps[k-i] += 1
        return count
    