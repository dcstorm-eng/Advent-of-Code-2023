# Advent of Code 2023
# D. Storm
# 12/04/2023

# Day 2.1

import re

sample_file = open("day2_1_sample.txt", "r")

input_file = open("day2_1_input.txt", "r")

bag = {'red': 12, 'green': 13, 'blue': 14}

good_games = []

# Each game is a row, there are multiple sets in each game
for row in input_file:
    #print(row)
    
    valid_game = 0
    
    # Find the Game ID number
    game_id = int(row.split(':')[0].split()[1])
    #print("Game ID:", game_id)
    
    games = row.rstrip().split(':')[1].split(';')
    
    for game in games:
        #valid_game = 1
        game = game.split(',')
        #print("Game:", game)
        
        for cube in game:
            cube = cube.strip().split()
            
            if int(cube[0]) > bag[cube[1]]:
                #print("Impossible!")
                valid_game = 1
        #Find index that contains each color
            
    if valid_game == 0:
        good_games.append(game_id)

                
    #print()

total_good_games = sum(good_games)
print("Total of good game id's:", total_good_games)