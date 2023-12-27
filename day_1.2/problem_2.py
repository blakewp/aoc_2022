def solution(file_path):
    with open(file_path, 'rt') as file:
        meals = file.read().split("\n\n")
    
    elf_calories = []
    for elf in meals:
        calories = sum(map(int,elf.splitlines()))
        elf_calories.append(calories)
        sorted_cals = sorted(elf_calories)
        ans = sum(sorted_cals[-3:])
        print(ans)

solution('/home/blake/aoc_2022/day_1/input.txt')