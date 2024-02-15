class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        i = 0
        count = 0
        while i < len(points):
            c = i
            while i+ 1 < len(points) and points[c][1] >= points[i+1][0]:
                i += 1
            count += 1
            i += 1
        return count