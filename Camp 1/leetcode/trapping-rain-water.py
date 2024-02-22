class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        ans = 0
        while l < r:
            if maxl <= maxr:
                l += 1
                val = maxl - height[l]
                maxl = max(maxl, height[l])
            else:
                r -= 1
                val = maxr - height[r]
                maxr = max(maxr, height[r])
            ans += val if val > 0 else 0
            
        return ans
        