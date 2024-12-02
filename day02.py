"""
cadybaltz
12/02/2024
AoC 2024 Day 2
Part 1: 3349, 00:11:15
Part 2: 2364, 00:17:47
"""

def is_safe(vals):
    safe = True

    prev = vals[0]
    dec = True
    if vals[1] > prev:
        dec = False

    for x in range(1, len(vals)):
        curr = vals[x]
        if curr < prev and not dec:
            safe = False
            break
        if prev < curr and dec:
            safe = False
            break

        diff = abs(prev - curr)
        if diff == 0 or diff > 3:
            safe = False
            break

        prev = curr

    return safe

def pt_1_solution(lines):
    result = 0
    for line in lines:
        vals = [int(value) for value in line.split()]
        if is_safe(vals):
            result += 1

    return result


def pt_2_solution(lines):
    result = 0

    for line in lines:
        vals = [int(value) for value in line.split()]

        for i_to_remove in range(-1, len(vals)):
            vals_copy = vals.copy()
            if i_to_remove != -1:
                del vals_copy[i_to_remove]

            if is_safe(vals_copy):
                result += 1
                break
    return result



if __name__ == '__main__':
    test = False

    input = open("test.txt", "r") if test else open("input.txt", "r")

    lines = input.readlines()

    pt_1 = pt_1_solution(lines)
    pt_2 = pt_2_solution(lines)

    print("Part 1: " + str(pt_1))
    print("Part 2: " + str(pt_2))