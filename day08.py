"""
cadybaltz
12/08/2024
AoC 2024 Day 8
Part 1: 1707, 00:15:49
Part 2: 2324, 00:28:04
"""

def is_safe(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)
def pt_1_solution(lines):
    grid = []
    chars = {}
    for x in range(len(lines)):
        grid.append(list(lines[x].strip()))
        for y in range(len(lines[x])):
            if lines[x][y] != '.':
                if lines[x][y] in chars:
                    chars[lines[x][y]].append((x, y))
                else:
                    chars[lines[x][y]] = [(x, y)]

    anti = set()
    for char in chars.keys():
        locs = chars[char]
        for x in range(len(locs)):
            for y in range(x + 1, len(locs)):
                x_diff = (locs[x][0] - locs[y][0])
                y_diff = (locs[x][1] - locs[y][1])

                anti1 = (locs[y][0] - x_diff, locs[y][1] - y_diff)
                anti2 = (locs[x][0] + x_diff, locs[x][1] + y_diff)

                if is_safe(anti1[0], anti1[1], grid):
                    anti.add(anti1)
                if is_safe(anti2[0], anti2[1], grid):
                    anti.add(anti2)

    return len(anti)


def pt_2_solution(lines):
    grid = []
    chars = {}
    anti = set()
    for x in range(len(lines)):
        grid.append(list(lines[x].strip()))
        for y in range(len(lines[x])):
            if lines[x][y] != '.':
                if lines[x][y] in chars:
                    chars[lines[x][y]].append((x, y))
                else:
                    chars[lines[x][y]] = [(x, y)]

    for char in chars.keys():
        locs = chars[char]
        for x in range(len(locs)):
            for y in range(x + 1, len(locs)):
                x_diff = (locs[x][0] - locs[y][0])
                y_diff = (locs[x][1] - locs[y][1])

                anti1 = (locs[y][0] - x_diff, locs[y][1] - y_diff)
                anti2 = (locs[x][0] + x_diff, locs[x][1] + y_diff)
                anti3 = (locs[x][0] - x_diff, locs[x][1] - y_diff)
                anti4 = (locs[y][0] + x_diff, locs[y][1] + y_diff)

                if is_safe(anti3[0], anti3[1], grid):
                    anti.add(anti3)
                if is_safe(anti4[0], anti4[1], grid):
                    anti.add(anti4)

                while is_safe(anti1[0], anti1[1], grid):
                    anti.add(anti1)
                    anti1 = (anti1[0] - x_diff, anti1[1] - y_diff)
                while is_safe(anti2[0], anti2[1], grid):
                    anti.add(anti2)
                    anti2 = (anti2[0] + x_diff, anti2[1] + y_diff)
    return len(anti)


if __name__ == '__main__':
    test = False

    input = open("test.txt", "r") if test else open("input.txt", "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))