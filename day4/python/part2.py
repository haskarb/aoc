# --- Day 4: Camp Cleanup (Part 2) ---

# read in the input file
with open("input.txt") as f:
    content = f.readlines()


def create_pair(pair) -> tuple:
    p = pair.split("-")
    return (int(p[0]), int(p[1]))


def overlap_all(pair: str) -> bool:
    # split the pair into two strings

    pair = pair.split(",")
    first_start, first_end = create_pair(pair[0])
    second_start, second_end = create_pair(pair[1])

    # check if pairs are mutually exclusive
    if first_end < second_start or second_end < first_start:
        return False

    return True


count_pair = sum([overlap_all(pair) for pair in content])
print(count_pair)
