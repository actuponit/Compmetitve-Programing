class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        m = {0: 1}
        sum = 0
        count = 0
        for num in nums:
            sum = (num + sum) % k
            if sum in m:
                count += m[sum]
                m[sum] += 1
            else:
                m[sum] = 1 
            
        return count