class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t = 1 if answerKey[0] == "T" else 0
        f = 1 if answerKey[0] == "F" else 0
        s, e = 0, 0
        ans = 0
        
        while e < len(answerKey):
            nk = min(t, f)
            while k >= nk and e < len(answerKey):
                e += 1
                t += 1 if e < len(answerKey) and answerKey[e] == "T" else 0
                f += 1 if e < len(answerKey) and answerKey[e] == "F" else 0
                nk = min(t, f)
            ans = max(ans, e - s)
            m = "T" if t < f else "F"
            while s < len(answerKey) and k < nk:
                t -= 1 if answerKey[s] == "T" else 0
                f -= 1 if answerKey[s] == "F" else 0
                s += 1
                nk = min(t, f)
            
        return ans

            