# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:52:46 2018

@author: joecu
"""

x = 5
y = 10
if x < y:
    print("x is less than y")

# Unlike math, we need two seperate characters for ">=" and "<="
if (y >= x):
    print("y is greater than or equal to x")
    print("y is",y)
    print("x is",x)
   
# In some langugages "not equal" is "<>" and in others it is "!="
# How did I know which Python likes? I cheated and tried it both ways.
# And no, this is not really cheating - it's actually effective.
if (x != y):
    print("x is different than y")