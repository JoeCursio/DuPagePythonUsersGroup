# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:28:09 2020

@author: jcursio
"""

import csv
with open("example_csv.csv") as csvfile: #can't open? Don't do anything
    dates = []
    colors = []
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print("the entire row is:",row)
        print("the dates and colors are:",row[0],row[3],"\n")
        aDate = row[0]
        aColor = row[3]
        dates.append(aDate)
        colors.append(aColor)
    print(dates)
    print(colors)