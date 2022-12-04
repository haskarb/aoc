# read input from text file
with open("../input.txt") as f:
    all_energy = f.read().splitlines()


elf_energy = {}
i = 0
for energy in all_energy:
    if energy == "":
        i += 1
    else:
        if i not in elf_energy:
            elf_energy[i] = int(energy)
        else:
            elf_energy[i] += int(energy)

# print max value
print(max(elf_energy.values())) # Part 1

#top 3
top3 = sorted(elf_energy.values(), reverse=True)[:3]
print(sum(top3)) # Part 2
