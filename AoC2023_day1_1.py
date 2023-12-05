# Advent of Code 2023
# D. Storm
# 11/30/2023

# Day 1.1

sample_file = open("day1_1_sample.txt", "r")

input = open("day1_1_input.txt", "r")

values = []

for line in input:
    #print("line:", line)
    temp = ""
    for char in line:
        if char.isnumeric():
            #sample.append(char)
            temp += char
    #print("all numbers:",temp)
    
    # print("first:",temp[0])
    # print("last:",temp[-1])
    
    new = temp[0] + temp[-1]
    # print("cleaned temp:", new)
    values.append(int(new))
    # print()

print("Final values:", values)

# Sum up all values

total = sum(values)
print("Total:", total)