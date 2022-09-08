class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse(self, root):
        dump = Node(-1)
        p = root

        while p is not None:
            q = p.next

            p.next = dump.next
            dump.next = p

            p = q

        return dump.next

    # 递归
    def reverse2(self, root):
        if not root:
            return root
        if root.next is None:
            return root

        new_head = self.reverse(root.next)

        root.next.next = root
        root.next = None

        return new_head


lst = [3, 4, 1, 2, 5]

p = dumph = Node(-1)
for i in lst:
    p.next = Node(i)
    p = p.next

# root = Solution().reverse(dumph.next)

root = Solution().reverse2(dumph.next)

while root is not None:
    print(root.val)
    root = root.next
