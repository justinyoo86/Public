# Author: Justin Yoo
# Link: https://projecteuler.net/problem=1

# Prompt:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 # and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


multiples_list = []

# Iterate through all numbers up to 1000
for i in range(0,1000):
  if i % 3 == 0 or i % 5 == 0:
    multiples_list.append(i)
  else:
    print(str(i) + ' is not a multiple of 3 and 5.')
    continue

print('The list of multiples of 3 and 5 are ' + str(sum(multiples_list)))
print('The sum of multiples_list is ' + str(sum(multiples_list)))