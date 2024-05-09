# Advent of Code 2023
# D. Storm
# 05/07/2024

# Day 4.2

with open('day4_1_sample.txt', 'r') as f:
    sample_file = f.read()
    
with open('day4_1_input.txt', 'r') as f:
    input_file = f.read()
    
test_file = sample_file
test_file = input_file

test_file = test_file.split('\n')

stack = []

for row in test_file:
    #print(row)
    
    points = 0
    
    row = row.split(':')
    temp_row = row[1].split('|')
    new_row = [row[0], temp_row[0], temp_row[1]]
    
    for num in new_row[2].split():
        #print(num)
        if num in new_row[1].split():
            points += 1
    new_row.append(points)
    new_row.append(1)
    
    #print("Row Total:", new_row)
    stack.append(new_row)

# print()
# print(stack)
# print()

for i in range(len(stack)):
    print("card", i+1, "nums", stack[i][3])
    
    for j in range(i+1, i + 1 + stack[i][3]):
        #print(j)
        print("adding card", j+1)
        stack[j][4] += stack[i][4] *    1
        print(stack[j])
    print()
        
print()
print(stack)
print()


pile_total = 0

for card in stack:
    pile_total += card[4]
    
print("Pile Total:", pile_total)


