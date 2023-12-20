class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st, e = 0, len(s)-1
        while st<e:
            s[st], s[e] = s[e], s[st]
            st +=1
            e -= 1
            
        