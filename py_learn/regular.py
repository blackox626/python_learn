import re

# * 0个 或多个  0是可以 不要前面的a
r = re.match('a*bb', 'bbnnnn')
print(r)

s = 'email for me is blackox626@gmail.com'
match = re.findall('^[emrt].*', s)
print(match)

# () 分组,需要输出的部分  不加的话 前后的 div tag 也会输出
content = '<h>ddedadsad</h><div>graph</div>bb<div>math</div>cc'
pat = re.compile(r"<div>(.*)</div>")  # 贪婪模式
m = pat.findall(content)
print(m)  # 匹配结果为： ['graph</div>bb<div>math']
