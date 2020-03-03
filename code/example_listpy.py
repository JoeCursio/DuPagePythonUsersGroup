# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:32:50 2018

@author: joecu
"""

my_list = [ 1, 2, 3, 4, 5, 6, 7, 8 ]

# Show the entire list
print( my_list )

# View an element of the list. WARNING!!!
# Programmers are used to counting starting at zero and
# many programming langugages (C/C++/Java/etc) do so.
print( "element number one is", my_list[1] )
print( "element number zero is", my_list[0] )

# Change an element of the list
my_list[2] = 200
print( my_list )