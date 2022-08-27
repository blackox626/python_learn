'''
有序链表，找到只出现一次的数字
1->2->2->3->3->5
1,5
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


str = input()
lst = str.split(',')

root = p = Node(lst[0])
for i in lst[1:]:
    p.next = Node(i)
    p = p.next

stack = []
while root:
    top = root.val
    stack.append(root.val)

    q = root.next
    while q and q.val == top:
        stack.pop()
        q = q.next
    root = q

for i in stack:
    print(i)
