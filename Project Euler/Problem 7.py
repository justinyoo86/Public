# Author: Justin Yoo
# Link: https://projecteuler.net/problem=7

# Prompt:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001st prime number?

prime_number_test = 3
prime_number_list = [2]
testing_prime_number = 0

while len(prime_number_list) < 10001:

    for divisor in range(0, prime_number_test + 1):
        if divisor == 0 or divisor == 1:
            continue
        elif prime_number_test == divisor:
            print('Prime number ' + str(prime_number_test) + ' found.  Appending to prime_number_list and length is currently ' + str(len(prime_number_list)))
            prime_number_list.append(prime_number_test)
        elif prime_number_test % divisor == 0:
            break
    prime_number_test = prime_number_test + 2
    
print(prime_number_list[10000])
