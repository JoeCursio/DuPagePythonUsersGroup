# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:23:27 2018

@author: joecu
"""

def add_two_numbers(num1, num2):
    result = num1 + num2
    # I discovered that the numbers are printed with spaces. 
    print("the sum of", num1, "and", num2, "is", result)

# This depends on the fixed order.
add_two_numbers(1,2)

# This is using named parametets instead of a fixed order
add_two_numbers(num2 = 100,num1 = 200)

# This will not work because we need two parameters and
# there are only one.
#add_two_numbers(1)

# This will not work because there are three parameters
# and there is only supposed to be two.
#add_two_numbers(1,2,3)