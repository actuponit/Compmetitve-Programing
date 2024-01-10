class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(firstList)):
            for j in range(len(secondList)):
                if firstList[i][0] > secondList[j][1] or firstList[i][1] < secondList[j][0]:
                    continue
                ans.append([
                    max(firstList[i][0], secondList[j][0]),
                    min(firstList[i][1], secondList[j][1]),
                ])
        return ans