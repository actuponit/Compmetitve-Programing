class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target - 1
        moves = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 1:
                target -= 1
            else:
                maxDoubles -= 1
                target = target // 2
            moves += 1
        return moves + (target - 1)

        