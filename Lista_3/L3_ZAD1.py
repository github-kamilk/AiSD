def check_values(n, k, p):
    if n < 0 or k < 0 or k > n:
        raise ValueError("n and k should be positive!")
    elif p < 0 or p > 1:
        raise Exception("Probability should be greater than 0 and less than 1!")


def quick_power(p, n, count_mult=0):
    if n == 0:
        return [1, count_mult]
    elif n % 2 == 0:
        count_mult += 2
        return quick_power(p * p, n // 2, count_mult)
    else:
        count_mult += 2
        result = quick_power(p * p, n // 2, count_mult)
        return result[0] * p, result[1]


def probability(n, k, p):
    check_values(n, k, p)
    single_values = []
    a_0 = quick_power(1 - p, n)
    a_n = a_0[0]
    single_values.append(a_n)
    count_mult = a_0[1]

    for i in range(0, k):
        q = p * (n - i) / ((1 - p) * (i + 1))
        a_n *= q
        count_mult += 4
        single_values.append(a_n)

    prob = sum(single_values)
    return prob, count_mult
