import numpy as np
from scipy import linalg
import random
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import csv


class Fit_class:
    def __init__(self):
        pass

    def fit_fun(self, x, a):
        return a * x ** self.power

def time_checker(n):
    a = np.array([[random.randint(-100, 100) for _ in range(n)] for _ in range(n)])
    b = np.array([random.randint(-100, 100) for _ in range(n)])
    start = time.time()
    linalg.solve(a, b)
    stop = time.time()
    return stop - start


def plot(x, y):
    plt.plot(x, y, 'ro', label="Dane")
    plt.xlabel("Liczba niewiadomych")
    plt.ylabel("Czas wykonania [s]")
    plt.legend(loc='upper left')
    plt.title("Wykres czasu w zależności od ilości niewiadomych")
    plt.show()



def hypothesis_plot(x, y, func, popt):
    x2 = np.arange(1, x[-1])

    plt.plot(x, y, 'ro', label="Dane")
    plt.plot(x2, func(x2, *popt), label="Hipoteza")
    plt.xlabel("Liczba niewiadomych")
    plt.ylabel("Czas wykonania [s]")
    plt.legend(loc='upper left')
    plt.title("Wykres czasu w zależności od ilości niewiadomych")
    plt.show()


if __name__ == "__main__":
    n = [1000*i for i in range(1,14)]

    execution_times = []
    # for i in n:
    #     execution_times.append(time_checker(i))
    #
    # with open('execution_times', 'w', newline='') as myfile:
    #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #     wr.writerow(execution_times)

    with open('execution_times.csv', newline='') as f:
        reader = csv.reader(f)
        execution_times = [float(i) for i in list(reader)[0]]

    inst = Fit_class()
    inst.power = np.polyfit(np.log(n), np.log(execution_times),1)[0]

    plot(n, execution_times)
    plot(np.log(n), np.log(execution_times))
    popt, pcov = curve_fit(inst.fit_fun, n, execution_times)
    hypothesis_plot(n, execution_times,inst.fit_fun, popt)
