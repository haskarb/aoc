# --- Day 2: Rock Paper Scissors (Part2) ---

# read input file
with open("../input.txt") as f:
    scores = f.read().splitlines()

shape_dict = {"A": 1, "B": 2, "C": 3}
elf_dict = {"X": 1, "Y": 2, "Z": 3}

win_combinations = ["A Z", "B Z", "C Z"]
rec_win_action = {"A": "B", "B": "C", "C": "A"}

draw_combinations = ["A Y", "B Y", "C Y"]

rec_lose_action = {"A": "C", "B": "A", "C": "B"}

round_score = 0
for item in scores:
    round_score_symbols = item.split()

    if item in win_combinations:
        win_score = 6
        elf_score = shape_dict[rec_win_action[round_score_symbols[0]]]
    elif item in draw_combinations:
        win_score = 3
        elf_score = shape_dict[round_score_symbols[0]]
    else:
        win_score = 0
        elf_score = shape_dict[rec_lose_action[round_score_symbols[0]]]

    # print(win_score)
    round_score += win_score + elf_score
print(round_score)
# break
