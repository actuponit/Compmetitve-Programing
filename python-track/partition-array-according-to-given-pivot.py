class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than, greater_than = [], []
        pivots = 0
        for i in nums:
            if i > pivot:
                greater_than.append(i)
            elif i < pivot:
                less_than.append(i)
            else:
                pivots += 1

        return less_than + [pivot]*pivots + greater_than