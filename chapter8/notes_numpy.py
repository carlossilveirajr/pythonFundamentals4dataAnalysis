
## standard way of numpy import

import numpy as np

help(np.array)

vector1 = np.array(range(9))

print(vector1)
print(type(vector1))

lst = list(range(9))
print(type(lst))

# array are better in memory terms and allows to change items in a index

# vai apresentar um erro, pois não pode misturar os tipos
#  vector1[0] = "novo elemento"

vector2 = np.arange(0., 4.5, .5)
print(vector2)
print(vector2.dtype)


import matplotlib.pyplot as plt

plt.show((plt.hist(np.random.rand(1000))))
