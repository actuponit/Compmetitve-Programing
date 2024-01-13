class Solution:
    def balancedString(self, s: str) -> int:
        """
        QQWQWWWRQRRR
        """
        start = 0
        freq = Counter(s)
        actual = len(s) // 4
        excess = {}
        mini = len(s)
        for i in "QWER":
            if freq[i] > actual:
                excess[i] = freq[i] - actual
        if not excess: return 0
        for i in range(len(s)):
            if s[i] in excess:
                excess[s[i]] -= 1
            if all([e <= 0 for e in excess.values()]):
                while all([e <= 0 for e in excess.values()]):
                    if s[start] in excess: 
                        excess[s[start]] += 1
                    start += 1
                mini = min(mini, i-start+2)
        return mini
            