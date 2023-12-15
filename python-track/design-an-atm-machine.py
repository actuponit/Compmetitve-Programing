class ATM:

    def __init__(self):
        self.dict = {
            20: 0,
            50: 0,
            100: 0,
            200: 0,
            500: 0,
        }
        

    def deposit(self, banknotesCount: List[int]) -> None:
        count = [20, 50, 100, 200, 500]
        for i in range(5):
            self.dict[count[i]] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        count = [500, 200, 100, 50, 20]
        answer = [0, 0, 0, 0, 0]
        for i in range(5):
            d = 0
            if self.dict[count[i]] > 0 and count[i] <= amount:
                m = amount // count[i]
                amount -= m*count[i] if m <= self.dict[count[i]] else self.dict[count[i]]*count[i]              
                d = m if m<=self.dict[count[i]] else self.dict[count[i]]
                self.dict[count[i]] -= d
            answer[4-i] = d
        if amount == 0:
            return answer
        else:
            self.deposit(answer)
            return [-1]
            


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)