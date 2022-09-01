# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = h = ListNode(-1)
        p = list1
        q = list2
        while q is not None and q is not None:
            if p.val > q.val:
                h.next = q
                q = q.next
            else:
                h.next = p
                p = p.next

        if q is None:
            h.next = p
        else:
            h.next = q

        return dummy.next
