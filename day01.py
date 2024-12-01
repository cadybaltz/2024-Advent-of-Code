"""
cadybaltz
12/01/2024
AoC 2024 Day 1
Part 1: 543, 00:02:33
Part 2: 374, 00:03:47
"""

def create_sorted_lists(lines):
    left_list = list()
    right_list = list()
    for line in lines:
        vals = line.split()

        first = int(vals[0])
        sec = int(vals[1])
        left_list.append(first)
        right_list.append(sec)
    left_list.sort()
    right_list.sort()
    return left_list, right_list

def pt_1_solution(lines):
    result = 0
    left_list, right_list = create_sorted_lists(lines)

    for x in range(len(left_list)):
        result += abs(left_list[x] - right_list[x])

    return result


def pt_2_solution(lines):
    result = 0
    left_list, right_list = create_sorted_lists(lines)

    for val in left_list:
        total = right_list.count(val)
        result += total * val
    return result



if __name__ == '__main__':
    test = False

    input = open("test.txt", "r") if test else open("input.txt", "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))