# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        if not head or not head.next:
            return odd

        even = head.next
        evens = even
        new_head = ListNode(next=odd)
        while odd and even:
            odd.next = even.next
            if not odd.next:
                odd.next = evens
                return new_head.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evens
        return new_head.next
        
        