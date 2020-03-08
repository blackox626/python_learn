import numpy as np

price = np.array([[170, 177, 169], [150, 159, 153],
                  [24, 27, 26], [165, 170, 167],
                  [22, 23, 20], [155, 116, 157]])

a = price < 25

print(a)

price[a] = 0

print(price)
