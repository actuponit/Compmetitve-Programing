class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        arr = [0] * 2
        for i in bills:
            if i == 5:
                arr[0] += 1
            elif i == 10:
                if arr[0] < 1:
                    return False
                arr[0] -= 1
                arr[1] += 1
            else:
                if arr[0] > 0 and arr[1] > 0:
                    arr[1] -= 1
                    arr[0] -= 1
                elif arr[0] > 2:
                    arr[0] -= 3
                else:
                    return False
        return True