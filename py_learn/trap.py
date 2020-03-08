def f(a, b=[]):  # NO!
    print(b)
    return b


ret = f(1)
ret.append(1)
ret.append(2)
# 当再调用f(1)时，预计打印为 []
f(1)


# 但是却为 [1,2]


def del_item(lst, e):
    return [i for i in lst if i != e]  # NO!


print(del_item([1, 3, 3, 3, 5], 3))

# 深复制
a = [[1, 2] for _ in range(3)]
a[0][0] = 5
print(a)  # [[5, 2], [1, 2], [1, 2]]
# 浅复制
b = [[1, 2]] * 3
b[0][0] = 5
print(b)  # [[5, 2], [5, 2], [5, 2]]
