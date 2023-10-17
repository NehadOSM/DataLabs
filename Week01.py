# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:06:48 2023

@author: A_Neh
"""

print ('Hello, World!')


import csv

file_path = r'C:\Users\A_Neh\Desktop\TB_burden_countries_2014-09-29.csv'

# Initialize a counter
row_count = 0

# Open the file and count the rows
with open(file_path, 'r') as f:
    for row in csv.reader(f):
        row_count += 1

# Print the total number of rows
print(f'Total number of rows: {row_count}')