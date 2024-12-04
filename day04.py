"""
cadybaltz
12/04/2024
AoC 2024 Day 4
Part 1: 305, 00:03:24
Part 2: 5272, 00:42:13
"""


def is_safe(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def search(grid, x, y, x_offset, y_offset):
    for lett in range(3):
        x2 = x + (x_offset * (lett + 1))
        y2 = y + (y_offset * (lett + 1))

        if not is_safe(x2, y2, grid) or grid[x2][y2] != 'MAS'[lett]:
            return False

    return True
def search_x(grid, x, y):
    diagonals = [
        [(1, 1), (-1, -1)],
        [(1, -1), (-1, 1)]
    ]
    for diagonal in diagonals:
        first_letter, second_letter = diagonal

        if not (
            is_safe(first_letter[0] + x, first_letter[1] + y, grid) and
            is_safe(second_letter[0] + x, second_letter[1] + y, grid) and
            (
                (
                    grid[first_letter[0] + x][first_letter[1] + y] == 'M' and
                    grid[second_letter[0] + x][second_letter[1] + y] == 'S'
                ) or
                (
                    grid[first_letter[0] + x][first_letter[1] + y] == 'S' and
                    grid[second_letter[0] + x][second_letter[1] + y] == 'M'
                )
            )
        ):
            return False
    return True
def pt_1_solution(lines):
    result = 0
    grid = []
    for line in lines:
        curr = []
        for x in range(len(line)):
            curr.append(line[x])
        grid.append(curr)

    directions = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) != (0, 0)]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'X':
                for direction in directions:
                    if search(grid, x, y, direction[0], direction[1]):
                        result += 1
    return result


def pt_2_solution(lines):
    result = 0
    grid = []
    for line in lines:
        curr = []
        for x in range(len(line)):
            curr.append(line[x])
        grid.append(curr)

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'A':
                if search_x(grid, x, y):
                    result += 1

    return result


if __name__ == '__main__':
    test = False

    input = open("test.txt", "r") if test else open("input.txt", "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))
