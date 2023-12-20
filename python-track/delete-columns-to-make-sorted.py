class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            found = True
            c = strs[0][i]
            for j in strs:
                # print(j[i], c)
                if j[i] < c: 
                    found = False
                    break
                else:
                    c = j[i]
            if not found:
                count += 1

        return count
        