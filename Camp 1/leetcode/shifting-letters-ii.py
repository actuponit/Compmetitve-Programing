class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans = [0] * (len(s) + 1)
        
        for i in shifts:
            if i[2] == 0:
                ans[i[0]] -= 1
                ans[i[1] + 1] += 1
            else:
                ans[i[0]] += 1
                ans[i[1] + 1] -= 1
                
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        sol = alphabet[(alphabet.index(s[0]) + ans[0]) % 26]
        sum = ans[0]
        print(ans)
        for i in range(1, len(s)):
            sum += ans[i]
            sol += alphabet[(alphabet.index(s[i]) + sum)%26]
        return sol
    
# -1, 2, -1, 0, 0