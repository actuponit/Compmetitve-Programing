class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        for i in s[:k]:
            if i in 'aeiou':
                count += 1
        ans = count
        for i in range(len(s)-k):
            if s[i] in 'aeiou':
                count -= 1
            if s[i + k] in 'aeiou':
                count += 1
            ans = max(ans, count)
        return ans