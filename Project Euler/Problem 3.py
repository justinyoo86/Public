# Author: Justin Yoo
# Link: https://projecteuler.net/problem=3

# Prompt:
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


x = 600851475143
x_original = x
largest_prime_factor = 2

# Iterate through all numbers until it returns a modulus of zero.  That number
# then becomes the "new" x and largest_prime_factor resets to 2.  
# largest_prime_factor will keep ticking up until it finds a new number with 
# a zero modulus.
while x > largest_prime_factor:
    if x % largest_prime_factor == 0:
        x = x / largest_prime_factor
        print('New x is = ' + str(largest_prime_factor))
        largest_prime_factor = 2
    else:
      largest_prime_factor = largest_prime_factor + 1

print('The largest prime factor of ' + str(x_original) + ' is ' + str(largest_prime_factor))