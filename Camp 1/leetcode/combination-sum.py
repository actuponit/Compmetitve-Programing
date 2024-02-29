class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        def backtrack(path, s, idx):
            if s == self.target:
                sol.append(path.copy())
                return
            if s > self.target:
                return
            for i in range(idx, len(candidates)):
                if s + candidates[i] > self.target:
                    break
                
                path.append(candidates[i])
                backtrack(path, s+candidates[i], i)    
                path.pop()
        
        candidates.sort()
        sol = []
        backtrack([], 0, 0)
        return sol
