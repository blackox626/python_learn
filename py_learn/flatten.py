def flten(lst):
    f = []
    for i in lst:
        if type(i) is list:
            for j in flten(i):
                f.append(j)
        else:
            f.append(i)

    return f


a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
print(flten(a))


def flten_2(x):
    if type(x) is list:
        return [y for l in x for y in flten_2(l)]
    else:
        return [x]


f = lambda x: [y for l in x for y in flten_2(l)] if type(x) is list else [x]
print(f(a))
