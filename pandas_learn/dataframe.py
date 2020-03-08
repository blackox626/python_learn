import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))
print(df1)
print(df1.values)
print(df1.index)

symbol = ['BABA', 'JD', 'AAPL', 'MS', 'GS', 'WMT']
data = {'行业': ['电商', '电商', '科技', '金融', '金融', '零售'],
        '价格': [176.92, 25.95, 172.97, 41.79, 196.00, 99.55],
        '交易量': [16175610, 27113291, 18913154, 10132145, 2626634, 8086946],
        '雇员': [101550, 175336, 100000, 60348, 36600, 2200000]}
df2 = pd.DataFrame(data, index=symbol)
df2.name = '美股'
df2.index.name = '代号'
print(df2)

df2.to_csv("test.csv")

df3 = pd.read_csv('test.csv')
print(df3)

print(df2.价格)
print(df2['价格'])
print(df2[['价格', '雇员']])

print(df2['BABA':'BABA'])  # 不能用df2['BABA']
