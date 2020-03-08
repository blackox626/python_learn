# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 双指针 一趟循环
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        dummy.next = head
        p = q = dummy
        for i in range(n):
            p = p.next

        while p.next is not None:
            p = p.next
            q = q.next

        q.next = q.next.next

        return dummy.next

    # 递归 太鸡儿强了
    # global i 很关键，从后开始 计算
    def removeNthFromEnd2(self, head, n):
        global i
        if head is None:
            i = 0
            return None
        head.next = self.removeNthFromEnd(head.next, n)
        i += 1
        return head.next if i == n else head
