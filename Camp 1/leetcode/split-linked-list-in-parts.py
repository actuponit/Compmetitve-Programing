# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        size = n // k if n > k else 1
        firsts = n % k if n > k else 0
        ans = [None] * k
        index = 0
        curr = head
        for i in range(firsts):
            ans[index] = curr
            for i in range(size):
                curr = curr.next
            temp = curr.next
            curr.next = None
            curr = temp
            index += 1
        while curr:
            ans[index] = curr
            for i in range(size-1):
                curr = curr.next
            temp = curr.next
            curr.next = None
            curr = temp
            index += 1
        return ans