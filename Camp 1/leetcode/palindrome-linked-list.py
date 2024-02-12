# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr, p = head, head
        while curr != None and curr.next!=None:
            curr = curr.next.next
            p = p.next
        mid = None
        temp = ListNode(-1, None)
        while p:
            temp.next = p.next
            p.next = mid
            mid = p
            p = temp.next
        curr = head
        while mid:
            if mid.val != curr.val:
                return False
            curr = curr.next
            mid = mid.next
        return True
        
        