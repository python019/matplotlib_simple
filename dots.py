import matplotlib.pyplot as pp
import numpy as np
import random

x = []
y = []

for _ in range(1000):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))

    pp.xlim(0, 100)
    pp.ylim(0, 100)
    pp.scatter(x, y, color="crimson")
    pp.pause(0.0001)

pp.show()
