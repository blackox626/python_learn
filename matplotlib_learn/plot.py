import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt

fig = plt.figure()
fig.add_axes()

# plt.plot([0, 2], [0, 1])
# plt.show()

# plt.subplots()

# plt.subplot(1, 2, 1)
# plt.text(0, 0, '1')
#
# plt.subplot(1, 2, 2)
# plt.text(0, 1, '2')
#
# plt.show()


symbol = ['BABA', 'JD', 'AAPL', 'MS', 'GS', 'WMT']
data = {'行业': ['电商', '电商', '科技', '金融', '金融', '零售'],
        '价格': [176.92, 25.95, 172.97, 41.79, 196.00, 99.55],
        '交易量': [16175610, 27113291, 18913154, 10132145, 2626634, 8086946],
        '雇员': [101550, 175336, 100000, 60348, 36600, 2200000]}
df2 = pd.DataFrame(data, index=symbol)

price = df2['价格']

# plt.plot(price.values)


ax = plt.subplot()
ax.plot(price.values)
ax.set_xticks(range(1, 50, 3))

plt.show()
