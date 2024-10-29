"""
Name:  Ashleigh Wong
Email:  ashleigh.wong12@myhunter.cuny.edu
Resources: Used python.org as a reminder of Python 3 print statements.
"""
def gcd(first_num, second_num):
    """
    Helper function to compute the greatest common divisor (GCD) of two numbers.
    """
    while first_num % second_num != 0:
        old_first = first_num
        old_second = second_num
        first_num = old_second
        second_num = old_first % old_second
    return second_num

class Fraction:
    """
    A class to represent fractions, from ThinkCS Chapter 18.
    """
    def __init__(self, numerator, denominator):
        """
        Initializes a Fraction instance with a numerator and denominator.
        """
        self.num = numerator      # numerator of the fraction
        self.den = denominator    # denominator of the fraction

    def __str__(self):
        """
        Returns a string representation of the fraction.
        """
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        """
        Reduces the fraction by dividing both the numerator and denominator
        by their greatest common divisor.
        """
        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common

    def __add__(self, other_fraction):
        """
        Adds two fractions and returns the result in simplified form.
        """
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        """
        Compares two fractions for equality.
        """
        return self.num * other.den == other.num * self.den

    def __mul__(self, other):
        """
        Multiplies two fractions and returns the simplified product.
        """
        new_num = self.num * other.num
        new_den = self.den * other.den
        result = Fraction(new_num, new_den)
        result.simplify()
        return result
#End-of-file (EOF)
