import pandas as pd

porfolio1 = pd.DataFrame({'Asset': ['FX', 'FX', 'IR'],
                          'Instrument': ['Option', 'Swap', 'Option'],
                          'Number': [1, 2, 3]})

porfolio2 = pd.DataFrame({'Asset': ['FX', 'FX', 'FX', 'IR'],
                          'Instrument': ['Option', 'Option', 'Swap', 'Swap'],
                          'Number': [4, 5, 6, 7]})
print(porfolio1)
print(porfolio2)

print(pd.merge(porfolio1, porfolio2, on='Asset'))
