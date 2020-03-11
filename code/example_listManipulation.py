# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:52:30 2020

@author: jcursio
"""

myList = [7,6,5,4,3,2,1]
print("the list is:", myList)
print( "the third element is", myList.index(2) )   #start counting from 0
print( "the number of 7s are:", myList.count(7) )
print("\n")

myList.append(7)
print("the list is:", myList)
print( "the third element is", myList.index(2) )    #start counting from 0
print( "the number of 7s are:", myList.count(7) )
print("\n")

print("the list is:", myList)
myList.remove(7)    #removes the first 7
print("the list is:", myList)
myList.remove(7)    #removed the next one
print("the list is:", myList)
print("\n")

names = ["Zena", "Hercules", "Plato", "Amazon"]
print("names are", names)
names.sort()
print("sorted names are", names)