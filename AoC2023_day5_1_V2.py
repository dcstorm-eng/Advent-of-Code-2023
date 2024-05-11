# Advent of Code 2023
# D. Storm
# 05/11/2024

# Day 5.1

with open('day5_1_sample.txt', 'r') as f:
    sample_file = f.read()
    
with open('day5_1_input.txt', 'r') as f:
    input_file = f.read()
    
test_file = sample_file
test_file = input_file

test_file = test_file.split('\n')

''' We know seeds are in first row, get the list of seeds we're looking for '''

input_seeds = test_file[0].split()
input_seeds.remove('seeds:')
input_seeds = [int(seed) for seed in input_seeds]

max_seed_number = max(input_seeds)

''' Get locations of the other info '''
headers = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']
   
# Header format: destination range start, source range start, range length

def check_seed(seed):
    seed_data = [seed]
    
    for i in range(len(headers)):
        #print("i:", i)
        header = headers[i]
        #print("Header:", header)
        
        # Find index where the header text is + 1 (first row of data)
        index = test_file.index(header) + 1
                        
        check_number = seed_data[-1]
        #print("check number:", check_number)
        
        while index < len(test_file) and test_file[index] != '':
            #print("index:", index)
            next_row = [int(row) for row in test_file[index].split()]
            dest_range_start, source_range_start, range_length = next_row
            
            #print("checking row", next_row)    

            if check_number >= source_range_start and check_number < source_range_start + range_length:
                seed_data.append(dest_range_start + check_number - source_range_start)
                #print("adding", seed_data[-1])
            
            index += 1
        
        if len(seed_data) <= (i + 1) :
            seed_data.append(check_number)
            #print("not found, adding", check_number)
        
        #print(seed_data)
        
    return seed_data

print()

# Format: [seed, soil, fertilizer, water, light, temperature, humidity, location]
all_seeds = []

for seed in input_seeds:
    print("Seed:", seed)
    
    seed_data = check_seed(seed)
    all_seeds.append(seed_data)
    
    print("Seed data:", seed_data)
    print()

#print("All Seeds:", all_seeds)

# TODO: Find min in location column and print

min_seed = min([row[-1] for row in all_seeds])

print("Min seed is:", min_seed)