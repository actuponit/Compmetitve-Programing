class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k >= len(cardPoints):
            return sum(cardPoints)

        left,right,mini,tot = 0,0, sum(cardPoints), 0

        while right < len(cardPoints):
            while right - left + 1 <= len(cardPoints) - k:
                tot += cardPoints[right]
                if right - left + 1 == len(cardPoints) - k:
                    mini = min(tot,mini)
                right += 1

            while right - left + 1 > len(cardPoints) - k:
                tot -= cardPoints[left]
                left += 1

        return sum(cardPoints) - mini 
                
"""
1 3 4 5 6 7 2 4 1
9 
"""