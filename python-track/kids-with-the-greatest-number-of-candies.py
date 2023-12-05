class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies =  max(candies)
        answer = []
        for i in candies:
            if i + extraCandies >= max_candies:
                answer.append(True)
            else:
                answer.append(False)
        return answer