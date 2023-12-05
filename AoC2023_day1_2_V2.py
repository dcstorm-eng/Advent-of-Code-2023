# Advent of Code 2023
# D. Storm
# 11/30/2023

# Day 1.2 - Try 2

import pandas as pd
import re

sample_file = open("day1_2_sample.txt", "r")

input_file = open("day1_1_input.txt", "r")

# with open("day1_1_input.txt") as myfile:
#     input_file=myfile.readlines()[0:10]

nums = {"one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9   }

values = []

for row in input_file:
    print(row)
    
    row_values = []
    
    # Find all integers
    
    for i in range (0, len(row), 1):
        character = row[i]
        #print(character)
        if character.isnumeric():
            row_values.append([i, character])
            
    #print("Row Values - ints:", row_values)
            
    # Find all numbers that are spelled out
    for num in nums:
        #print("checking num:", num)
        for i in range (0, len(row)-len(num), 1):
            test = row[i:i+len(num)]
            #print(test)
            if test == num:
                #print("found num", num, "at index:", i)
                row_values.append([i, nums[num]])
    
    #print("Row Values - both:", row_values)
    
    # Sort by index
    row_values.sort(key=lambda tup: tup[0])
    
    #print("Row Values - sorted:", row_values)
    
    # Add first and last to values list 
    row_values = "" + str(row_values[0][1]) + str(row_values[-1][1])
    
    print("Row Values - first and last:", row_values)
    
    values.append(int(row_values))
    
# Sum up all row values
total = sum(values)
print("Total:", total)
            
            