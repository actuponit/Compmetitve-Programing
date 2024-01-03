class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        ans = 0
        j = 0
        for i in range(0, len(tasks), 4):
            ans = max(tasks[i] + processorTime[j], ans)
            j += 1
        return ans
        