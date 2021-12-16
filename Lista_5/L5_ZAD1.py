import numpy as np
from scipy import linalg
import random
import time


def create_matrix(n):
    a = np.array([[random.randint(-100, 100) for _ in range(n)] for _ in range(n)])
    b = np.array([random.randint(-100, 100) for _ in range(n)])
    return linear_solving(a, b)


def linear_solving(a, b):
    x = linalg.solve(a, b)
    return x


def time_checker(n):
    execution_times = []
    for i in range(1, n):
        start = time.time()
        create_matrix(i)
        stop = time.time()
        execution_times.append(stop - start)
    return execution_times


print(time_checker(1000))
