# Author: Justin Yoo
# Link: https://projecteuler.net/problem=8

# Prompt:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pythagorean_triplet_checker(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False

product_abc = 0

# Pick arbitrary maximum values for a and b.  Since the sum of a + b + c needs
# to equal 1000, choose 1000 as the maximum number.
for a in range(1,1000):
    for b in range(1,1000):
        if a > b:
            continue
        else:
            for c in range(1,1000):
                if a > c or b > c:
                    continue
                else:
                    is_pythagorean_triplet = pythagorean_triplet_checker(a, b, c)
                    if is_pythagorean_triplet == True:
                        if a + b + c == 1000:
                            product_abc = a * b * c
                            print('a is ' + str(a) + ' b is ' + str(b) + ' c is ' + str(c))
                            print(product_abc)
                            break