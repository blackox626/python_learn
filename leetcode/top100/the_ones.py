# coding=utf-8
import sys

# 1,1,2,2,3,4,4,5,5,7

str = input()
print(str)


# print('Hello,World!')

class node:
    def __init__(self, val):
        self.val = val
        self.next = None


# lst = [1, 2, 2, 3, 3, 5]
lst = str.split(',')
head = p = node(lst[0])
for i in lst[1:]:
    p.next = node(i)
    p = p.next

result = []

# i = head
# j = i.next
# while j is not None:
#     if i.val != j.val:
#         print(i.val)
#         i = i.next
#         j = i.next
#     else:
#         j = j.next
#         while j and j.val == i.val:
#             j = j.next
#         i = j
#         if not i:
#             break
#         j = j.next
#         if not j:
#             print(i.val)

i = head
while i is not None:
    j = i.next
    if not j:
        print(i.val)
        break
    if i.val != j.val:
        print(i.val)
        i = i.next
        j = i.next
    else:
        while j and j.val == i.val:
            j = j.next
        i = j
