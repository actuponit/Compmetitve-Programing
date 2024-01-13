class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, maxf = 0, 0 
        l = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = 1+count.get(s[r], 0)
            maxf = max(count[s[r]], maxf)
            
            while ((r-l+1) - maxf) > k:
                count[s[l]] -= 1
                l += 1
                
                
            ans = max(ans, (r-l+1))
        return ans
        """
        max = A
        ABABBABB
         ^  ^
        map maxfreq and other
        """