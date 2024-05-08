# Advent of Code 2023
# D. Storm
# 05/07/2024

# Day 4.1

with open('day4_1_sample.txt', 'r') as f:
    sample_file = f.read()
    
with open('day4_1_input.txt', 'r') as f:
    input_file = f.read()
    
test_file = sample_file
test_file = input_file

test_file = test_file.split('\n')

stack = []



for row in test_file:
    print(row)
    
    points = 0
    
    row = row.split(':')
    temp_row = row[1].split('|')
    new_row = [row[0], temp_row[0], temp_row[1]]
    
    for num in new_row[2].split():
        #print(num)
        if num in new_row[1].split():
            if points == 0:
                points += 1
            else:
                points = 2 * points 
    new_row.append(points)
    
    #print("Row Total:", new_row)
    stack.append(new_row)

pile_total = 0

for card in stack:
    pile_total += card[3]
    

print("Pile Total:", pile_total)