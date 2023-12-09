class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        ones = []
        for i in range(len(boxes)):
            if boxes[i] == '1':
                ones.append(i)
        for i in range(len(boxes)):
            s = 0
            for j in ones:
                s += abs(j - i)
            
            answer.append(s)
        
        return answer
        