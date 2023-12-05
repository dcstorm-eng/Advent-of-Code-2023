# Advent of Code 2023
# D. Storm
# 11/30/2023

# Day 1.2

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

def findall(p, s):
    '''Yields all the positions of
    the pattern p in the string s.'''
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)
        
values = []

# for line in sample_file:
for line in input_file:
    print("line:", line)
    
    # find index of written out numbers
    number_index = []
    for key in nums:
        
        if key in line:
            index = line.index(key)
            
            index = [i for i, x in enumerate(line) if x == key]
            
            #print("key:", key, ",index:", index)
            number_index.append([index, nums[key]])
            
    #print("Nums:", number_index)
    
    # Add numbers with index
    
    for i in range(0,len(line)-1,1):
        #print("char:", line[i])
        if line[i].isnumeric():
            number_index.append([i, int(line[i])])
            
    #print("Nums:", number_index)
    
    # Sort by index
    #number_index.sort(key=lambda tup: tup[0])
    print("Sorted Nums:", number_index)
    
    # Drop all but the first and last values
    
    new = "" + str(number_index[0][1]) + str(number_index[-1][1])
    
    print("Cleaned up line:", new)
    
    values.append(int(new))
    # print()

print("Final values:", values)

# Sum up all values

total = sum(values)
print("Total:", total)