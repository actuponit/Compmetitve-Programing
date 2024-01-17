class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        no_whites = 0
        for i in range(k):
            no_whites += 1 if blocks[i] == "W" else 0
        ans = no_whites
        for i in range(k, len(blocks)):
            no_whites += 1 if blocks[i] == "W" else 0
            no_whites -= 1 if blocks[i-k] == "W" else 0
            ans = min(no_whites, ans)
        return ans
        