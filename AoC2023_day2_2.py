# Advent of Code 2023
# D. Storm
# 12/04/2023

# Day 2.2

import pandas as pd
import math

sample_file = open("day2_1_sample.txt", "r")

input_file = open("day2_1_input.txt", "r")

total = 0

# Each game is a row, there are multiple sets in each game
for row in input_file:
    #print(row)
    
    min_cubes_dict = {'red':0, 'blue':0, 'green':0}
    
    # Find the Game ID number
    game_id = int(row.split(':')[0].split()[1])
    #print("Game ID:", game_id)
           
    games = row.rstrip().split(':')[1].split(';')
           
    for game in games:
        game = game.split(',')  
        #print("Game:", game)
        
        for cube in game:
            cube = cube.strip().split()
            cube[0] = int(cube[0])
            if int(cube[0]) > min_cubes_dict[cube[1]]:
                min_cubes_dict[cube[1]] = cube[0]
        
    total += math.prod(min_cubes_dict.values())

print("Total:", total)