class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        mini = float('inf')
        duplicates = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                duplicates.add(fronts[i])
        
        for i in range(len(fronts)):
            if backs[i] <= mini and backs[i] not in duplicates:
                mini = backs[i]
            if fronts[i] <= mini and fronts[i] not in duplicates:
                mini = fronts[i]

        return mini if mini != float('inf') else 0