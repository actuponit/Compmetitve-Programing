class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        count = 0
        p = 0
        for i in range(len(nums)):
               
            while p+1 < nums[i] and p < n:
                count += 1
                # print(p)
                p += p + 1
                # print(p)
            p += nums[i]
            if p >= n:
                break
        while p < n:
            p += p + 1
            count += 1
        return count
        