class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map = {}
        count = 0
        for i in range(len(nums)):
            if map and nums[i] in map:
                map[nums[i]] += 1
                count += map[nums[i]]
            else:
                map[nums[i]] = 0
        return count 
"""
0 2
3 1
1 2 1

1 2 1+2+3 

"""