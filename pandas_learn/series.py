import pandas as pd

s = pd.Series([11, 22, 33, 44])
print(s)
print(s.values)
print(s.index)

dates = pd.date_range('20190401', periods=4)
s1 = pd.Series([27.2, 27.65, 27.70, 28], index=dates)
print(s1)
print(s1.values)
print(s1.index)

data_dict = {'BABA': 187.07, 'PDD': 21.83, 'JD': 30.79, 'BIDU': 184.77}

s2 = pd.Series(data_dict)
s3 = pd.Series(data=data_dict, index=['FB', 'BABA', 'PDD', 'JD'])

print(s3.index)

print(s2, '\n', s3)

print(s2 + s3)  # 相加之后 baidu 为 NaN了  FB 为 Nan 好理解


