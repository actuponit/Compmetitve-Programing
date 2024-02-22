class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st = [-1]
        pref = [0] * len(arr)
        for i in range(len(arr)):
            while st[-1] > -1 and arr[st[-1]] > arr[i]:
                st.pop()
             
            pref[i] = i - st[-1]
            st.append(i)
        st2 = [-1]
        print(pref)
        a = arr[::-1]
        for i in range(len(arr)):
            while st2[-1] > -1 and a[st2[-1]] >= a[i]:
                st2.pop()
             
            pref[len(arr)-i-1] *= i - st2[-1]
            # print(i - st2[-1])
            st2.append(i)
        # print(pref)
        sum = 0
        for i in range(len(arr)):
            sum += pref[i] * arr[i]
        return sum % ((10 ** 9) + 7)