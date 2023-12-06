class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        cw, ccw = 0, 0
        condition = False
        for i in range(len(distance)):
            idx = (start + i)%len(distance)            
            if idx == destination or condition:
                ccw += distance[idx]
                condition = True
            elif idx != destination:
                cw += distance[idx]

        return min(cw, ccw) 