class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in s:
            temp = ''
            if i != ']':
                st.append(i)
            else:
                while st[-1] != '[':
                    temp = st.pop() + temp
                st.pop()
                num = ''
                while st and st[-1].isdigit():
                    num = st.pop() + num
                num = int(num)
            
                # Push them back to the stack    
                for i in (num * temp):
                    st.append(i)
        return ''.join(st)