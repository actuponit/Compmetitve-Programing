class Solution:
    def average(self, salary: List[int]) -> float:
        salary_sum = sum(salary)-min(salary)-max(salary)
        return salary_sum / (len(salary) - 2)
        
        