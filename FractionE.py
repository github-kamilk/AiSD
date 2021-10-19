from decimal import *
import math


def greatest_common_measure(a, b):
    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    else:
        gcd = b
    return gcd


def float_to_fraction(x):
    x_str = str(float(x))
    decimal_place = abs(Decimal(x_str).as_tuple().exponent)
    num = int(x * (10 ** decimal_place))
    den = 10 ** decimal_place
    return FractionE(num, den)


class FractionE():
    def __init__(self, num, den):
        if type(num) == int and type(den) == int and den != 0:
            gcd = greatest_common_measure(num, den)
            self.numerator = num // gcd
            self.denominator = den // gcd
        elif type(num) == float or type(den) == float:
            num = float_to_fraction(num)
            den = float_to_fraction(den)
            new_fraction = num / den
            self.numerator = new_fraction.get_num()
            self.denominator = new_fraction.get_dem()
        elif den == 0:
            raise ValueError("Can't divide by 0.")
        else:
            raise ValueError("Wrong data given.")

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def mixed(self, x=True):
        if x == True:
            if self.numerator * self.denominator < 0:
                absolute_value_numerator = math.fabs(self.numerator)
                absolute_value_denominator = math.fabs(self.denominator)
                if absolute_value_numerator > absolute_value_denominator:
                    return str((self.numerator // self.denominator) + 1) + "(" + str(
                        FractionE(self.denominator - (self.numerator % self.denominator), self.denominator)) + ")"
                else:
                    return str(self.numerator) + "/" + str(self.denominator)
            else:
                if self.numerator > self.denominator:
                    return str(self.numerator // self.denominator) + "(" + str(
                        FractionE(self.numerator % self.denominator, self.denominator)) + ")"
                else:
                    return str(self.numerator) + "/" + str(self.denominator)
        else:
            return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator + self.denominator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return FractionE(new_numerator, new_denominator)

    def __radd__(self, other):
        other = float_to_fraction(other)
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return FractionE(new_numerator, new_denominator)

    def __sub__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator - self.denominator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return FractionE(new_numerator, new_denominator)

    def __rsub__(self, other):
        other = float_to_fraction(other)
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return FractionE(new_numerator, new_denominator)

    def __mul__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return FractionE(new_numerator, new_denominator)

    def __rmul__(self, other):
        other = float_to_fraction(other)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return FractionE(new_numerator, new_denominator)

    def __truediv__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        return FractionE(new_numerator, new_denominator)

    def __rtruediv__(self, other):
        other = float_to_fraction(other)
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return FractionE(new_numerator, new_denominator)

    def __lt__(self, other):
        if type(other) == float:
            other = float_to_fraction(other)
        return (self.numerator * other.denominator < other.numerator * self.denominator)

    def __gt__(self, other):
        if type(other) == float:
            other = float_to_fraction(other)
        return (self.numerator * other.denominator > other.numerator * self.denominator)

    def __le__(self, other):
        if type(other) == float:
            other = float_to_fraction(other)
        return (self.numerator * other.denominator <= other.numerator * self.denominator)

    def __ge__(self, other):
        if type(other) == float:
            other = float_to_fraction(other)
        return (self.numerator * other.denominator >= other.numerator * self.denominator)

    def __eq__(self, other):
        if type(other) == float:
            other = float_to_fraction(other)
        return (self.numerator * other.denominator == other.numerator * self.denominator)

    def __ne__(self, other):
        if type(other) == float:
            other = float_to_fraction(other)
        return (self.numerator * other.denominator != other.numerator * self.denominator)

    def get_num(self):
        return self.numerator

    def get_dem(self):
        return self.denominator
