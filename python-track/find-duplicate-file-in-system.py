class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        mp = {}
        for s in paths:
            x = s.split()
            root = x[0]
            for i in range(1, len(x)):
                opening_bracket = x[i].index('(')
                file_name = x[i][:opening_bracket]
                content = x[i][opening_bracket+1: len(x[i])-1]

                mp[content] = mp.get(content, []) + [root+'/'+file_name]
        answer = []
        for k, v in mp.items():
            if len(v) > 1: answer.append(v)
        return answer
        