def test(str='yes'):
    print(str.upper() + "!")


a = test

del test

a('no')
test()

print([x for x in range(10)])
