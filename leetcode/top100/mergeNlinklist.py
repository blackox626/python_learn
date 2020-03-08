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

    # 普通解法 ： 循环遍历 每个 链表  找到最小的
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        p = dummp = ListNode(-1)

        stop = False

        while not stop:
            min = None
            minIndex = None
            for i, list in enumerate(lists):
                if min is None or (list is not None and list.val < min.val):
                    min = list
                    minIndex = i

            p.next = min
            if min is not None:
                p = p.next
                if min.next is None:
                    del lists[minIndex]
                else:
                    lists[minIndex] = min.next
            else:
                stop = True

        return dummp.next

    # 优化...  递归
    def mergeKLists2(self, lists):
        min = None
        minIndex = None
        for i, list in enumerate(lists):
            if min is None or (list is not None and list.val < min.val):
                min = list
                minIndex = i

        if min is not None:

            if min.next is None:
                del lists[minIndex]
            else:
                lists[minIndex] = min.next

            min.next = self.mergeKLists2(lists)

        return min

    def mergeKLists3(self, lists):
        n = len(lists)
        if n == 0: return None
        # if n == 1: return lists[0]

        step = 1

        while step < n:
            for i in range(0, n, step * 2):
                lists[i] = self.mergeTwoLists2(lists[i], lists[i + step] if i + step < n else None)
            step *= 2

        return lists[0]

    def mergeTwoLists2(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists2(l1.next, l2)

        return l1 or l2


re = Solution().mergeKLists3([ListNode([1, 4, 5]), ListNode([1, 3, 4]), ListNode([2, 6])])

while re is not None:
    print(re.val)
    re = re.next
