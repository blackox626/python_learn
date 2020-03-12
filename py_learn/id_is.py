# coding:utf-8
# /usr/bin/python
"""
2018-11-03
dinghanhua
变量，数据类型
"""

'''python是弱类型语言，变量无需指定数据类型
所有的变量都是引用类型，是内存地址指针，保持的是内存中对象的地址
内存中对象分为可变类型和不可变类型'''

'''不可变数据类型如整数、浮点数、字符串、布尔值、元组
一样的值赋值给不同的变量指向同一个地址'''
i = 100
j = 100
str1 = 'string'
str2 = 'string'
turple1 = (1, 2, 3)
turple2 = (1, 2, 3)
'''id()打印变量地址,is判定变量是否指向同一个内存地址'''
print(id(i), id(j), id(i) == id(j), i is j)
print(id(str1), id(str2), id(str1) == id(str2), str1 is str2)
print(id(turple1), id(turple2), id(turple1) == id(turple2), turple1 is turple2)

'''可变数据类型如list,dict
一样的值赋值给不同的变量指向不同的地址'''
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1), id(list2), id(list1) == id(list2), list1 is list2)

set1 = {1, 2, 3}
set2 = {1, 2, 3}
print(id(set1), id(set2), id(set1) == id(set2), set1 is set2)

dict1 = {'title': "python", "date": "2018-11-03"}
dict2 = {'title': "python", "date": "2018-11-03"}
print(id(dict1), id(dict2), id(dict1) == id(dict2), dict1 is dict2)
