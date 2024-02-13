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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode cur = new ListNode();
        ListNode ans = cur;
        while (list1 != null || list2 != null ) {
            if (list1 != null && list2 != null) {
                if(list1.val < list2.val) {
                    cur.next = new ListNode(list1.val, null);
                    list1 = list1.next;
                } else {
                    cur.next = new ListNode(list2.val, null);
                    list2 = list2.next;
                }
            }
            else if (list1 == null) {
                cur.next = new ListNode(list2.val, null);
                list2 = list2.next;
            }
            else {
                cur.next = new ListNode(list1.val, null);
                list1 = list1.next;
            }
            cur = cur.next;
        }
        return ans.next;
    }
}