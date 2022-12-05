# --- Day 3: Rucksack Reorganization ---

# read the input file
with open('../input.txt', 'r') as f:
    rucksacks = f.read().splitlines()


def priorites(rucksack):
    #divide the input into two lists
    size = len(rucksack)
    rucksack1 = rucksack[:size//2]
    rucksack2 = rucksack[size//2:]

    # find common items
    common = set(rucksack1).intersection(rucksack2)

    # find the common item with the highest priority
    for item in common:
        if item.isupper():
            return ord(item)-38
        else:
            return ord(item)-96

priority_sum = sum([priorites(rucksack) for rucksack in rucksacks])
print(priority_sum)

