# --- Day 4: Camp Cleanup ---

# read in the input file
with open("input.txt") as f:
    content = f.readlines()


def create_pair(pair) -> tuple:
    p = pair.split("-")
    return (int(p[0]), int(p[1]))


def full_contained_pair(pair: str) -> bool:
    # split the pair into two strings
    pair = pair.split(",")
    first_start, first_end = create_pair(pair[0])
    second_start, second_end = create_pair(pair[1])

    if first_start >= second_start and first_end <= second_end:
        return True
    elif second_start >= first_start and second_end <= first_end:
        return True

    return False


total_pair = sum([full_contained_pair(pair) for pair in content])
print(total_pair)
