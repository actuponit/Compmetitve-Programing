class Solution:
    def largestGoodInteger(self, num: str) -> str:
        answer = ''
        cur_max = -1
        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                if int(num[i]) > cur_max:
                    answer = 3*num[i]
                    cur_max = int(num[i])
        return answer