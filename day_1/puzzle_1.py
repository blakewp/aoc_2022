#!/bin/python3

def solution(file_path):
    with open(file_path, 'rt') as file:
        meals = file.read().split("\n\n")
    
    elf_calories = []
    for elf in meals:
        calories = sum(map(int,elf.splitlines()))
        elf_calories.append(calories)
        print(max(elf_calories))

solution('/home/blake/aoc_2022/day_1/input.txt')

