class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        i = len(s) - 1
        ans = ""
        while (i > -1):
            if s[i] == '#':
                i -= 2
                index = int("".join([s[i], s[i+1]]))
            else:
                index = int(s[i])
            ans = alphabet[index-1] + ans
            i -= 1

        return ans