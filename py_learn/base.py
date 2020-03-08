for i in range(0, 10, 2):
    print(i)

print(max([5, 4, 3]))

# 一行反转 step 为负数 ，反向
ls = [1, 2, 3]
print(ls[::-1])

# 一行代码求多个列表中的最大值
max(max([[1, 2, 3], [5, 1], [4]], key=lambda v: max(v)))  # 5

range(10, -1, -1)

s = "print('helloworld')"
r = compile(s, "<string>", "exec")
exec(r)

from collections import Counter


def find_all_duplicates(lst):
    # value -> count
    c = Counter(lst)
    # k 即为value list的值为符合要求的k
    return list(filter(lambda k: c[k] > 1, c))


print(find_all_duplicates([1, 3, 3, 4, 4, 4]))

# Counter 构造函数参数 必须为可迭代的对象
mapc = map(Counter, [[1], [2], [3]])

for ic in mapc:
    print(ic)


def sumc(*c):
    if (len(c) < 1):
        return
    mapc = map(Counter, c)
    s = Counter([])
    for ic in mapc:  # ic 是一个Counter对象
        s += ic
    return s


a = ['apple', 'orange', 'computer', 'orange']
b = ['computer', 'orange']

# Counter({'orange': 3, 'computer': 3, 'apple': 1, 'abc': 1, 'face': 1})
sumc(a, b, ['abc'], ['face', 'computer'])

m = map(lambda i: print(i), [1, 2, 3])

for p in m:
    print(p)

# python3 不在内置函数中
from functools import reduce

reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
