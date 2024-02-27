class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 0
        # 0 1
        # 0 1 2
        # 0 1 2 3 4
        # 0 1 2 3 4 5
        # def pascal(row)
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        arr = self.getRow(rowIndex - 1)
        new = [1 for i in range(rowIndex+1)]
        for i in range(1, len(arr)):
            new[i] = arr[i] + arr[i-1]
        return new
        