/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(-1, head);
        ListNode prev = dummy;
        for (int pos=0;pos<left-1;pos++)
            prev = prev.next;
        ListNode curr = prev.next;
        for(int pos=left; pos<right; pos++) {
            ListNode forw = curr.next;
            curr.next = forw.next;
            forw.next = prev.next;     
            prev.next = forw;
            }
         return dummy.next;          
    }
}