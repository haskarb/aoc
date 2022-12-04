# --- Day 2: Rock Paper Scissors ---

# read input file
with open("../input.txt") as f:
    scores = f.read().splitlines()

shape_dict = {"A": 1, "B": 2, "C": 3}
elf_dict = {"X": 1, "Y": 2, "Z": 3}

win_combinations = ["A Y", "B Z", "C X"]
draw_combinations = ["A X", "B Y", "C Z"]


round_score = 0
for item in scores:
    if item in win_combinations:
        win_score = 6
    elif item in draw_combinations:
        win_score = 3
    else:
        win_score = 0

    round_score_symbols = item.split()
    pl_score = shape_dict[round_score_symbols[0]]
    elf_score = elf_dict[round_score_symbols[-1]]

    round_score += win_score + elf_score
print(round_score)
# break
