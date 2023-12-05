class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0

        for i in range(1, len(points)):
            point1, point2 = points[i-1], points[i]
            max_time = max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))
            total_time += max_time

        return total_time

# 2+3, 4 