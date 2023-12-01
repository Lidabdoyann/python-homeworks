#xndir 2
from fractions import Fraction

def add_fractions(frac1, frac2):
    result = frac1 + frac2
    return result

def subtract_fractions(frac1, frac2):
    result = frac1 - frac2
    return result

def multiply_fractions(frac1, frac2):
    result = frac1 * frac2
    return result

def divide_fractions(frac1, frac2):
    result = frac1 / frac2
    return result

# Example usage:
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

sum_result = add_fractions(fraction1, fraction2)
difference_result = subtract_fractions(fraction1, fraction2)
product_result = multiply_fractions(fraction1, fraction2)
quotient_result = divide_fractions(fraction1, fraction2)

print(f"{fraction1} + {fraction2} = {sum_result}")
print(f"{fraction1} - {fraction2} = {difference_result}")
print(f"{fraction1} * {fraction2} = {product_result}")
print(f"{fraction1} / {fraction2} = {quotient_result}")