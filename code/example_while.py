# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:04:03 2018

@author: joecu
"""

# everything indented gets repeated.
counter = 1
while counter<= 10:
    print("the count is", counter)
    counter = counter + 1
    
print("the final value is", counter)

# Beware of repeating forever: hit <CNTL><c> to stop or the red square.
unchanging = 1
while unchanging < 2:
    print("repeat again and...")

# this is a bad example:
counter = 1
while counter<= 10:
    print("the count is", counter)
counter = counter + 1       # because this is not indented, it is not repeated.
    
# A technique to stop accidental typos: use "+=" or "-=" 
# For example, instead of "counter = counter + 1" say 'counter += 1"
# If you misspelled counter once, then Python creates another 
# different variable for you.
typo = 1
while typo < 5:
    print("This was not supposed to go forever", typo)
    typo = tyypo + 1
    