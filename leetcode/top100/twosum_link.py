# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val):
        if isinstance(val, int):
            self.val = val
            self.next = None

        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result, ahead = ListNode(0), 0
        theResult = result
        while l1 is not None or l2 is not None:
            sum, ahead = self.add(l1, l2, ahead)
            result.next = ListNode(sum)
            result = result.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if ahead > 0:
            result.next = ListNode(ahead)
        return theResult.next

    def add(self, l1, l2, ahead=0):
        x = 0 if l1 is None else l1.val
        y = 0 if l2 is None else l2.val
        sum = x + y + ahead
        ahead = sum // 10
        sum = sum % 10
        return sum, ahead


result = Solution().addTwoNumbers(ListNode([1, 8]), ListNode([0]))

print(result)
