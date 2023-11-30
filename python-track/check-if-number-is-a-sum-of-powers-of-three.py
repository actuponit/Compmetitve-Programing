class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            reminder = n % 3
            if reminder == 2:
                return False
            n = n // 3
        return True     