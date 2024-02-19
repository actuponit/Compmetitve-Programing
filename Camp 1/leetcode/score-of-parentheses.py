class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        st = []
        for i in s:
            if i == '(':
                st.append(score)
                score = 0
            elif i == ')':
                score = st.pop() + max(2*score, 1)
        return score