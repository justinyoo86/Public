# Author: Justin Yoo
# Link: https://projecteuler.net/problem=8

# Prompt:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def prime_number_generator (prime_number_target, target_lesser_or_greater):
    
    prime_number_test = 1
    
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
    
    return prime_number_list
