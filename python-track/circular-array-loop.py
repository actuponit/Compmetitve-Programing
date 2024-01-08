class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            j = 0
            s = i+nums[i]
            if s % len(nums) == i: continue
            while j < len(nums):
                s %= len(nums)
                if nums[s] * nums[i] < 0: break
                s += nums[s]
                if s == i or s % len(nums) == i:
                    print(s, i)
                    return True
                j += 1
        return False
                