def greatest_common_divisor(a, b):
    while a % b != 0:
        temp = a % b
        a = b
        b = temp
    else:
        gcd = b
    return gcd


class Fraction():
    def __init__(self, num, den):
        if type(num) == int and type(den) == int and den != 0:
            gcd = greatest_common_divisor(num, den)
            self.numerator = num // gcd
            self.denominator = den // gcd
        elif den == 0:
            raise ValueError("Can't divide by 0.")
        else:
            raise ValueError("Wrong data given.")

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator + self.denominator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator - self.denominator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        return Fraction(new_numerator, new_denominator)

    def __lt__(self, other_fraction):
        return (self.numerator * other_fraction.denominator < other_fraction.numerator * self.denominator)

    def __gt__(self, other_fraction):
        return (self.numerator * other_fraction.denominator > other_fraction.numerator * self.denominator)

    def __le__(self, other_fraction):
        return (self.numerator * other_fraction.denominator <= other_fraction.numerator * self.denominator)

    def __ge__(self, other_fraction):
        return (self.numerator * other_fraction.denominator >= other_fraction.numerator * self.denominator)

    def __eq__(self, other_fraction):
        return (self.numerator * other_fraction.denominator == other_fraction.numerator * self.denominator)

    def __ne__(self, other_fraction):
        return (self.numerator * other_fraction.denominator != other_fraction.numerator * self.denominator)

    def get_num(self):
        return self.numerator

    def get_dem(self):
        return self.denominator


f1 = Fraction(1, 5)
f2 = Fraction(1, 5)
print(f1-f2)
