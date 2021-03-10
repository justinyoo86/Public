# Author: Justin Yoo
# Link: https://projecteuler.net/problem=5

# Prompt:
# 2520 is the smallest number that can be divided by each of the numbers from 
# 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?

testing_quotient = 2520
testing_condition = False
highest_quotient_match = 2520
highest_testing_count = 0

# This will take a number (testing_quotient, starting at 2520) and test 
# whether it is evenly divisible by the numbers from 1 to 20.  If it is, it 
# will continue attempting to divide testing_quotient by the next number in
# the sequence of 1 to 20.  The number of evenly divided test cases are logged
# in testing_count.  The highest testing_count and highest quotient are stored
# in highest_testing_count and highest_testing_quotient, respectively.  This 
# while loop will continue until the testing_count reaches 20.

while testing_condition == False:
    testing_count = 1
    for divisor in range(1,21):
        if testing_quotient % divisor == 0:
            testing_count = testing_count + 1
                        
            if testing_count >= highest_testing_count:
                highest_testing_count = testing_count
                highest_quotient_match = testing_quotient
                print('The highest testing count is ' + str(highest_testing_count) + ' and it belongs to the highest quotient match of ' + str(highest_quotient_match))
            
            if testing_count == 20:
                testing_condition = True
                break
            continue
        else:
            testing_quotient = testing_quotient + 20
            break