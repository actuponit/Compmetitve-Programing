# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        left = dummy
        right = dummy
        while right and right.next:
            if left.next.val < x:
                left = left.next
                right = right.next
            elif right.next.val < x:
                temp = right.next
                right.next = temp.next
                temp.next = left.next
                left.next = temp
                left = left.next
            else:
                right = right.next
        return dummy.next

            
        