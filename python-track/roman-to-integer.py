class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        prev = 2000
        for i in s:
            if i == "I":                
                ans += 1
                prev = 1
            elif i == "V":
                if prev < 5:
                    ans -= 2
                ans += 5
                prev = 2000
            elif i == "X":
                if prev < 10:
                    ans -= 2
                ans += 10
                prev = 10
            elif i == "L":
                if prev < 50:
                    ans -= 20
                ans += 50
                prev = 2000
            elif i == "C":
                if prev < 100:
                    ans -= 20
                ans += 100
                prev = 100
            elif i == "D":
                if prev < 500:
                    ans -= 200
                ans += 500
                prev = 2000
            elif i == "M":
                if prev < 1000:
                    ans -= 200
                ans += 1000
                prev = 2000
            
        return ans
"""
IX
"""