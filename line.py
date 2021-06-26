import matplotlib.pyplot as pp
import numpy as np
from sklearn.linear_model import LinearRegression
import random

reg = LinearRegression()

x = []
y = []

for i in range(1000):
    pp.clf()
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))

    x_v = np.array(x)
    x_v = x_v.reshape(-1, 1)

    y_v = np.array(y)
    y_v = y_v.reshape(-1, 1)

    if i % 20 == 0:
        reg.fit(x_v, y_v)
        pp.xlim(0, 100)
        pp.ylim(0, 100)
        pp.scatter(x, y, color="crimson")
        pp.plot(list(range(100)), reg.predict(np.array([x for x in range(100)]).reshape(-1,1)))
        pp.pause(0.0001)

pp.show()

