# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        map = {}
        i=0
        while curr:
            if map and curr in map:
                return curr
            map[curr] = curr
            curr=curr.next
        return None
            
            
        