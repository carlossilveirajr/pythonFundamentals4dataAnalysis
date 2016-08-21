import pandas as pd

obj = pd.Series([4, 7, -5, 2])

print(obj)

# series array unidimensional que possui um sequencia e indices
print(obj.values)
print(obj.index)

obj2 = pd.Series([4, 7, -5, 2], index=['a', 'b', 'c', 'd'])
print(obj2)

print(obj2[obj2 > 3])

print('d' in obj2)

# dicinarios podem ser convertidos em series e a chaves viram os indices

data = {"Estado": ["SP", "MG", "RJ"],
        "Ano": [9, 10, 11],
        "Populacao" : [0.123, 132.123, 123.26]
        }

frame = pd.DataFrame(data)
print(frame)

frame2 = pd.DataFrame(data, columns=["Estado", "Ano", "Populacao", "Debito"])
print(frame2)
print(frame2["Estado"])


import numpy as np

frame2["Debito"] = np.arange(3.)

print(frame2)

print(frame2.describe())

