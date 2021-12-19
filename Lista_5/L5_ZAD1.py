import numpy as np
from scipy import linalg
import random
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math


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


def func(x, a, b, power=2):
    return a * x ** power + b


def plot(x, y):
    plt.plot(x, y, 'ro', label="Dane")
    plt.xlabel("Liczba niewiadomych")
    plt.ylabel("Czas wykonania [s]")
    plt.legend(loc='upper left')
    plt.title("Wykres czasu w zależności od ilości niewiadomych")
    plt.show()


def log_plot(x, y):
    plt.loglog(x, y, 'ro', label="Dane")
    plt.xlabel("Liczba niewiadomych")
    plt.ylabel("Czas wykonania [s]")
    plt.legend(loc='upper left')
    plt.title("Wykres czasu w zależności od ilości niewiadomych")
    plt.show()


def hypothesis_plot(x, y, popt):
    x2 = np.arange(1, x[-1])

    plt.plot(x, y, 'ro', label="Dane")
    plt.plot(x2, func(x2, *popt), label="Hipoteza")
    plt.xlabel("Liczba niewiadomych")
    plt.ylabel("Czas wykonania [s]")
    plt.legend(loc='upper left')
    plt.title("Wykres czasu w zależności od ilości niewiadomych")
    plt.show()


def doubling(x_tab, y_tab):
    ratio = [None] * len(y_tab)
    for i in range(1, len(y_tab)):
        if y_tab[i - 1] != 0:
            ratio[i] = y_tab[i] / y_tab[i - 1]
        else:
            ratio[i] = 0
    lratio = [None]
    for val in ratio:
        if val:
            lratio.append(math.log(val, 2))
        else:
            lratio.append(None)

    print("{} \t {} \t {} \t {}".format("N", "T", "Ratio", "Log"))
    for i in range(len(y_tab)):
        print("{} \t {} \t {} \t {}".format(x_tab[i], y_tab[i], ratio[i], lratio[i]))


if __name__ == "__main__":
    n = [2 ** i for i in range(1, 11)]
    execution_times = []
    for i in n:
        execution_times.append(time_checker(i))

    # plot(n, execution_times)
    # log_plot(n, execution_times)
    popt, pcov = curve_fit(func, n, execution_times)
    print(popt)
    doubling(n, execution_times)
    hypothesis_plot(n, execution_times, popt)
