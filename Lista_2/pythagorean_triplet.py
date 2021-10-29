import math


def version_1(sum):
    k = 0
    for a in range(1, sum):
        for b in range(1, sum):
            for c in range(1, sum):
                k += 9
                if a + b + c == sum and a ** 2 + b ** 2 == c ** 2:
                    return (True, a, b, c, k)
    return (False, None, None, None, k)


def version_2(sum):
    x = int(sum / 3)
    y = int(sum / 2)
    k = 4
    for a in range(1, x):
        for b in range(1, y):
            k += 7
            c = sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return (True, a, b, c, k)
    return (False, None, None, None, k)


def version_3(sum):
    x = int(sum / 3)
    y = int(sum / 2)
    k = 4
    for a in range(1, x):
        for b in range(a, y):
            k += 7
            c = sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return (True, a, b, c, k)
    return (False, None, None, None, k)


def version_4(sum):
    k = 0
    for c in range(1, sum):
        k += 7
        a_b_squared = c ** 2 - sum ** 2 + 2 * sum * c
        if a_b_squared > 0:
            k += 4
            a_b = math.floor(math.sqrt(a_b_squared))
            if a_b * a_b == a_b_squared:
                k += 5
                b = (sum - c + a_b) / 2
                a = sum - b - c
                k += 3
                if a > 0 and b > 0:
                    return (True, a, b, c, k)
    return (False, None, None, None, k)


def version_5(sum):
    k = 3
    for c in range(math.floor(sum / 3 + 1), sum):
        k += 7
        a_b_squared = c ** 2 - sum ** 2 + 2 * sum * c
        if a_b_squared > 0:
            k += 4
            a_b = math.floor(math.sqrt(a_b_squared))
            if a_b * a_b == a_b_squared:
                k += 5
                b = (sum - c + a_b) / 2
                a = sum - b - c
                k += 3
                if a > 0 and b > 0:
                    return (True, a, b, c, k)
    return (False, None, None, None, k)
