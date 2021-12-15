import numpy as np
from scipy import linalg
import time

a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

x = linalg.solve(a, b)
print(x)

def linear_solving(a,b):
    x = linalg.solve(a, b)
    return x

def time_checker(n):
    pass
