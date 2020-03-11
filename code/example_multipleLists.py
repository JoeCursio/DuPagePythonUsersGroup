# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:04:53 2020

@author: jcursio
"""

xMatrix = [ [1,2], [3,4], [5,6], [7,8] ] # a list of lists
print(xMatrix)
print(xMatrix[1]) #start counting from 0
print(xMatrix[3][0]) #fourth row, first element

print(xMatrix)
xMatrix.reverse()   #reverse each element in the main list
print(xMatrix)

for eachThing in xMatrix:   #each thing is another list inside
    eachThing.reverse()     #reverse each list inside
print(xMatrix)
    
    