# Author: Justin Yoo
# Link: https://projecteuler.net/problem=6

# Prompt:
# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural 
# numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.

sum_square_of_number = 0
sum_of_number = 0

for number in range(1,101):
    sum_square_of_number = sum_square_of_number + (number ** 2)
    sum_of_number = sum_of_number + number

square_sum_of_number = sum_of_number ** 2

difference = square_sum_of_number - sum_square_of_number
print(difference)