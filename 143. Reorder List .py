‘’‘
https://leetcode.com/problems/reorder-list/discuss/44992/Java-solution-with-3-steps
’‘’

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None

        # find middle
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        p1, p2, slow.next=head, slow.next, None

        # reverse the latter
        cur = p2
        prev = None
        while cur:
            cur.next, cur, prev = pre, cur.next, cur
        p2 = prev

        # merge
        dummy = cur = ListNode(0)
        while p1 or p2:
            if p1: cur.next, p1, cur = p1, p1.next, p1
            if p2: cur.next, p2, cur = p2, p2.next, p2
        return dummy.next
