# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        curr, next = head, head.next
        
        while curr and next:
            if curr.val <= next.val:
                curr = curr.next
                next = next.next
                continue
            while prev.next and prev.next.val < next.val:
                prev = prev.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next
            
            prev = dummy
            next = curr.next
        return dummy.next

        