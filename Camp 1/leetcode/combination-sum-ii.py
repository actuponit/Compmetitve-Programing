class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path, s, idx):
            # print('here:',s,idx,path)
            if s == self.target:
                sol.append(path.copy())
                return
            if s > self.target:
                return
            for i in range(idx, len(candidates)):
                if s+candidates[i] > self.target:
                    return
                if self.prev == candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(path, s+candidates[i], i+1)
                self.prev = path.pop()
        self.prev = 0
        candidates.sort()
        sol= []
        self.target = target
        backtrack([], 0, 0)
        return sol