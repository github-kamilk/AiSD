import math


def version_1(sum):
    k = 0
    for a in range(1, sum):
        for b in range(1, sum):
            for c in range(1, sum):
                k += 9
                if a + b + c == sum and a ** 2 + b ** 2 == c ** 2:
                    print(True, a, b, c, k)
                    return 0
    print(False, None, None, None, k)


def version_2(sum):
    k = 2
    for a in range(1, int(sum / 3)):
        k+=2
        for b in range(1, int(sum / 2)):
            k += 7
            c = sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(True, a, b, c, k)
                return 0
    print(False, None, None, None, k)

def version_3(sum):
    k = 2
    for a in range(1, int(sum / 3)):
        k+=3
        for b in range(a, int(sum / 2)):
            k += 7
            c = sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(True, a, b, c, k)
                return 0
    print(False, None, None, None, k)

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
                k+=3
                if a>0 and b>0:
                    print(True, a, b, c, k)
                    return 0
    print(False, None, None, None, k)

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
                k+=3
                if a>0 and b>0:
                    print(True, a, b, c, k)
                    return 0
    print(False, None, None, None, k)

version_1(1000)
version_2(1000)
version_3(1000)
version_4(1000)
version_5(1000)
