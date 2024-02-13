class Solution:
    def minimumSteps(self, s: str) -> int:
        seeker, p = 0, 0
        swap = 0
        for p in range(len(s)):
            while seeker < len(s) and s[seeker] == '1':
                seeker += 1
            swap += (seeker - p) if seeker < len(s) else 0
            seeker += 1 
                
        return swap
        