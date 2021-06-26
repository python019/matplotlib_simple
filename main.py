import matplotlib.pyplot as pp
import numpy as np
from sklearn.linear_model import LinearRegression
import random

x = []
y = []

for i in range(1000):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))

    x_v = np.array(x)
    x_v = x.reshape(-1, 1)

    y_v = np.array(y)
    y_v = y.reshape(-1, 1)

    if i % 5 == 0:
        pp.xlim(0, 100)
        pp.ylim(0, 100)
        pp.scatter(x, y, color="crimson")
        pp.pause(0.0001)

pp.show()

