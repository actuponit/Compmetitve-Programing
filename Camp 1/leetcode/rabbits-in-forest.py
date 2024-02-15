class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        i = 0
        ans = 0
        while i < len(answers):
            c = 1
            while i + 1 < len(answers) and answers[i] == answers[i+1] and c < answers[i] + 1:
                c += 1
                i += 1
            ans += answers[i] + 1
            i += 1
        return ans
        