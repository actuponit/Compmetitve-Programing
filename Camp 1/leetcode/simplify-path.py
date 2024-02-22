class Solution:
    def simplifyPath(self, path: str) -> str:
        # print("/home///..".split('/'))
        path = path.split('/')
        st = []
        for i in path:
            if not i or i == '.':
                continue
            if i == '..':
                if st: st.pop()
                continue
            st.append(i)

        return '/' + '/'.join(st)