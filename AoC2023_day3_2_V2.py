# Advent of Code 2023
# D. Storm
# 05/07/2024

# Day 3.2

import numpy as np
import re
from operator import mul

with open('day3_1_sample.txt', 'r') as f:
    sample_file = f.read()
    
with open('day3_1_input.txt', 'r') as f:
    input_file = f.read()

# with open('day3_1_temp.txt', 'r') as f:
#     input_file = f.read()
    
test_file = sample_file
test_file = input_file

test_file = test_file.split('\n')

''' Use input file to get list of all symbols '''
symbol_list = []

for row in input_file:
    row = row.rstrip()
    for char in row:
        if not char.isnumeric() and char not in symbol_list and char != '.':
            symbol_list.append(char)
            
''' Expand test file to eliminate edge cases '''
test_file.insert(0, ".".ljust(len(test_file[0]), "."))
test_file.append(".".ljust(len(test_file[0]), "."))

rows = len(test_file)
cols = len(test_file[0])

temp = []
for row in test_file:
    temp.append("." + row + ".")

test_file = temp

''' Find part numbers in test file '''
all_numbers = []

for i in range(rows):
    row = test_file[i].strip()
    #print("Row", i, ":", row)
    
    for sym in symbol_list:
        row = row.replace(sym, ' ')
    
    #print("new row:", row)
    
    start = 0
    j = 0

    while j <= cols:
        start = j
        num = ""
        while j <= cols and row[j].isdigit():
            num += row[j]
            j += 1

        if num == "":
            j += 1
            continue

        num = int(num)
                        
        all_numbers.append([num, i, start, start - 1 + len(str(num))]) # FORMAT: [Number, Row, Start Index, End Index]
        
''' Check if Part Number ''' 

part_numbers = []

for number in all_numbers:
    number_temp, number_row, number_start_index, number_end_index = number
    
    is_pn = 0
    
    #print("Number", number_temp, "row", number_row ,"start_index", number_start_index, "end_index", number_end_index)
    
    # check test file around number to find symbols
    for j in range(number_row - 1, number_row + 2): # Rows = i-1 to i+1
        #print("check row", j)
        for k in range(number_start_index - 1, number_end_index + 2): # Columns index - 1 to index + length of number + 1
            #print("check index", k, ":", test_file[j][k])
            if test_file[j][k] in symbol_list:
                #print(test_file[j][k], "found at", j, k)
                is_pn += 1
    
    if is_pn > 0:
        #print("Part Number Found")
        part_numbers.append([number_temp, number_row, number_start_index, number_end_index])
    #else:
        #print("Not a P/N")
    #print()

''' Function to check cells around given location and return gear ratio if 2 found '''
def check_neighbors(check_row, check_col):
    is_gear = 0
    return_pns = []
    
    for pn in part_numbers:
        pn_temp, pn_row, pn_start_index, pn_end_index = pn
        print("Checking", pn_temp, "at row", pn_row, ":", pn_start_index, "-", pn_end_index)
        
        if abs(pn_row - check_row) <= 1 and check_col >= (pn_start_index - 1) and check_col <= (pn_end_index + 1):
            print("Found Gear!")
            is_gear += 1
            return_pns.append(pn)
    

    
    if is_gear > 1:
        print("Gear Found")
        #part_numbers.append(int(number_temp))
        return return_pns
    else:
        print("Not a Gear")
        return 0
    #print()

''' find all instances of '*' and call check neighbors fucntion'''
sum_gear_ratios = 0

for i in range(rows):
    row = test_file[i].strip()
    print("Row", i, ":", row)
    
    for j in range(cols):
        char = test_file[i][j]
        print(j, char)
        
        if char == '*':
            print("Found * at row", i, "col", j)
            result = check_neighbors(i,j)
            print("result:", result)
            
            if result:
                sum_gear_ratios += int(result[0][0]) * int(result[1][0])
            
#print("Total:", sum(part_numbers))

print("Sum of Gear Ratios:", sum_gear_ratios)    