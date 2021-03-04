# Author: Justin Yoo
# Link: https://projecteuler.net/problem=4

# Prompt:
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

largest_palindrome = 0;
palindrome = 0;

# The largest product will have a range between 5 to 6 digits.  Iterate through
# all 3-digit numbers from 100 to 999.  Python is exclusive of the last number
# in a range function, so we will enter 1000 and it will only call up to 999.
for i in range(100, 1000):
  for j in range(100, 1000):
    product = i * j
    
    # Convert product to a string so that character comparisons are possible.
    string = str(product)
    
    # For products that are 5 digits in length.  Compare the first and last 
    # numbers and the second and second to last numbers and see if they are 
    # equal.  The middle number does not need to be compared. If the numbers
    # are equal, store the product in largest_palindrome the two factors into 
    # i_saved and j_saved, respectively.
    if len(str(string)) == 5:
        if string[0] == string[4] and string[1] == string[3]:
            if product > largest_palindrome:
                largest_palindrome = product
                i_saved = i
                j_saved = j
    # Compare the first and last numbers, the second and second to last 
    # numbers, and the third and third to last numbers and see if they are 
    # equal.  If the numbers are equal, store the product in 
    # largest_palindrome the two factors into i_saved and j_saved, 
    # respectively.
    elif len(str(string)) == 6:
        if string[0] == string[5] and string[1] == string[4] and string[2] == string[3]:
            if product > largest_palindrome:
                largest_palindrome = product
                i_saved = i
                j_saved = j
                

print('The two 3-digit numbers that give the largest palindromic number are ' + str(i_saved) + ' and ' + str(j_saved))
print('The largest palindromic number is ' + str(largest_palindrome))