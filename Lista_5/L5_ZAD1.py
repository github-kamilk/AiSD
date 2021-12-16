import numpy as np
from scipy import linalg
import random
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def create_matrix(n):
    a = np.array([[random.randint(-100, 100) for _ in range(n)] for _ in range(n)])
    b = np.array([random.randint(-100, 100) for _ in range(n)])
    return linear_solving(a, b)


def linear_solving(a, b):
    x = linalg.solve(a, b)
    return x


def time_checker(n):
    start = time.time()
    create_matrix(n)
    stop = time.time()
    return stop - start


def func(x, a, b):
    return a * x ** 2 + b

def plot(x, y):
    plt.plot(x, y, 'ro', label="Dane")
    plt.xlabel("Liczba niewiadomych")
    plt.ylabel("Czas wykonania [s]")
    plt.legend(loc='upper left')
    plt.title("Wykres zależności czasu od ilości niewiadomych")
    plt.show()


def log_plot(x, y):
    plt.loglog(x, y, 'ro', label="Dane")
    plt.xlabel("Liczba niewiadomych")
    plt.ylabel("Czas wykonania [s]")
    plt.legend(loc='upper left')
    plt.title("Wykres zależności czasu od ilości niewiadomych")
    plt.show()

def hypothesis_plot(x, y, popt):
    x2 = np.arange(1, x[-1])

    plt.plot(x, y, 'ro', label="Dane")
    plt.plot(x2, func(x2, *popt), label="Hipoteza")
    plt.xlabel("Liczba niewiadomych")
    plt.ylabel("Czas wykonania [s]")
    plt.legend(loc='upper left')
    plt.title("Wykres zależności czasu od ilości niewiadomych")
    plt.show()


if __name__ == "__main__":
    n = [2 ** i for i in range(1, 14)]
    execution_times = []
    for i in n:
        execution_times.append(time_checker(i))

    # log_plot(n, execution_times)
    popt, pcov = curve_fit(func, n, execution_times)
    hypothesis_plot(n, execution_times,popt)
