from fractions import Fraction
from math import gcd

class Rational(object):
    ''' This class will create rational numbers. It can also display and
    perform some operations on them '''
    def __init__(self):
        self.numerator = 0
        self.denominator = 1

    def prompt_nums(self):
        self.numerator = int(input("Enter the numerator: "))
        self.denominator = int(input("Enter the denominator: "))

    def display(self):
        if self.numerator < self.denominator:
            print (str(self.numerator) + "/" + str(self.denominator))
        elif self.numerator > self.denominator:
            residual = int(self.numerator) % int(self.denominator)
            integer = int(self.numerator / self.denominator)
            print (str(integer) + " " + str(residual) + "/" + str(self.denominator))
        else:
            print (self.numerator / self.denominator)

    def display_decimal(self):
        print (str(self.numerator / self.denominator))

    def reductor(self):
        simple = Fr