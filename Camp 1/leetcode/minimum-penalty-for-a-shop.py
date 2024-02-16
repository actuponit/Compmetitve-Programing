class Solution:
    def bestClosingTime(self, customers: str) -> int:
        l = len(customers)
        y = [0] * (len(customers) + 1)
        n = [0] * (len(customers) + 1)
        for i in range(len(customers)):
            n[i + 1] = n[i] + (1 if customers[i] == 'N' else 0)
            y[l - i - 1] = y[l-i] + (1 if customers[l-i-1] == 'Y' else 0)
        min_index = 0
        min_val = n[0] + y[0]
        for i in range(l + 1):
            if min_val > n[i] + y[i]:
                min_val = n[i] + y[i]
                min_index = i
        return min_index
        