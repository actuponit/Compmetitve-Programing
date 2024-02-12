# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = set()
        while head:
            if prev and head in prev:
                return True
            prev.add(head)
            head = head.next
        return False
        