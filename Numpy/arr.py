import numpy as np
from numpy import random

arr = np.array([1,2,3,4,5,6])
print(arr)
print(type(arr))
print(np.__version__)

x = random.randint(100)
print(x)
f= random.rand()
print(f)
y = random.randint(1000, size = (100))
print(y)

