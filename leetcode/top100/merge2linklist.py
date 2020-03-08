# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 常规思路
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(-1)

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1 is not None:
            p.next = l1

        if l2 is not None:
            p.next = l2

        return dummy.next

    # 递归的思路，总是没那么容易想到。。
    def mergeTwoLists2(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists2(l1.next, l2)

        return l1 or l2
