def ordinary_polynomial_value_calc(coeff, arg):
    if not isinstance(coeff, list) or not isinstance(arg, (int, float)):
        raise TypeError("Wrong data given.")
    
    value = coeff[0]
    count_mult = 0
    count_add = 0
    for i in range(1, len(coeff)):
        value = value + (coeff[i]) * arg ** i
        count_mult += i
        count_add += 1
    return value, count_mult, count_add

def smart_polynomial_value_calc(coeff, arg):
    if not isinstance(coeff, list) or not isinstance(arg, (int, float)):
        raise TypeError("Wrong data given.")
    
    value = 0
    count_mult = 0
    count_add = 0 
    coeff.reverse()
    for i in coeff[:-1]:
        if value == 0:
            value = (i) * arg
            count_mult += 1
        else:
            value = (value + i) * arg
            count_add += 1
            count_mult += 1
    value += coeff[-1]
    count_add += 1
    return value, count_mult, count_add
