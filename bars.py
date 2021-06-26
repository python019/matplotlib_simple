import matplotlib.pyplot as pp
import random

values = [0] * 50

for i in range(50):
    values[i] =(random.randint(0,100))
    pp.xlim(0,50)
    pp.ylim(0,100)
    pp.bar(list(range(50)), values)
    pp.pause(0.0001)

pp.show()