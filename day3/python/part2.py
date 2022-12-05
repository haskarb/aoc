# --- Day 3: Rucksack Reorganization (Part 2) ---

# read the input file
with open('../input.txt', 'r') as f:
    rucksacks = f.read().splitlines()

def priorites(rucksack):
    #divide the input into three lists
    size = len(rucksack)
    rucksack1 = rucksack[0]
    rucksack2 = rucksack[1]
    rucksack3 = rucksack[2]

    # find common items in the three lists
    common = set(rucksack1).intersection(rucksack2, rucksack3)

    # find the common item with the highest priority
    for item in common:
        if item.isupper():
            return ord(item)-38
        else:
            return ord(item)-96

# create group of three rucksacks
sum_priorities = sum([priorites(rucksacks[i:i+3]) for i in range(0, len(rucksacks), 3)])
print(sum_priorities)

