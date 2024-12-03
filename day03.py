"""
cadybaltz
12/03/2024
AoC 2024 Day 3
Part 1: 190, 00:01:54
Part 2: 560, 00:07:31
"""

import re

pt1_pattern = r"mul\((\d+),(\d+)\)"
pt2_pattern = r"(mul|do|don't)\((?:(\d+),(\d+))?\)"

def pt_1_solution(lines):
    result = 0
    for line in lines:
        matches = re.findall(pt1_pattern, line)
        for match in matches:
            result += int(match[0]) * int(match[1])
    return result

def pt_2_solution(lines):
    result = 0
    do = True
    for line in lines:
        matches = re.findall(pt2_pattern, line)
        for match in matches:
            if match[0] == 'mul':
                one, num1, num2 = match
                if do:
                    result += int(num1) * int(num2)
            else:
                if match[0] == 'do':
                    do = True
                else:
                    do = False
    return result



if __name__ == '__main__':
    test = False
    input = open("test.txt", "r") if test else open("input.txt", "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))