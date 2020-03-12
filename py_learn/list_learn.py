def clone_runoob(li1):
    li_copy = li1[:]

    # li_copy = []
    # li_copy.extend(li1)

    # li_copy = list(li1)
    return li_copy


li1 = [4, 8, 2, 10, 15, 18]
li2 = clone_runoob(li1)

li1[0] = 5

print("原始列表:", li1)
print("复制后列表:", li2)
