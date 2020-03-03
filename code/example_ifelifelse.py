# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:52:46 2018

@author: joecu
"""

x = 5
y = 10

# this is a nested if statement: an if statement inside another
if x < y:
    print("x is less than y")
else:
    if x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")
        
        
# Another way
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
