"""
cadybaltz
12/09/2024
AoC 2024 Day 9
Part 1: 522, 00:10:57
Part 2: 1334, 00:41:43
"""

def pt_1_solution(lines):
    result = 0
    disk = []
    index = 0

    for line in lines:
        alt = True
        for val in line.strip():
            if alt:
                for x in range(int(val)):
                    disk.append(index)
                alt = False
                index += 1
            else:
                for x in range(int(val)):
                    disk.append(-1)
                alt = True
    leftmost = 0
    for i in range(len(disk) - 1, -1, -1):
        if disk[i] != -1:
            moved = False

            while not moved and leftmost < i:
                if disk[leftmost] == -1:
                    disk[leftmost] = disk[i]
                    disk[i] = -1
                    moved = True
                leftmost += 1

    x = 0
    for val in disk:
        if val > -1:
            result += val * x
        x += 1
    return result

def pt_2_solution(lines):
    result = 0
    disk = []
    index = 0
    index_to_size = {}
    index_to_start = {}

    for line in lines:
        alt = True
        for size in line.strip():
            if alt:
                start = len(disk)
                for x in range(int(size)):
                    disk.append(index)
                alt = False
                index_to_size[index] = int(size)
                index_to_start[index] = start
                index += 1
            else:
                for x in range(int(size)):
                    disk.append('.')
                alt = True
    index -= 1

    for i in range(index, -1, -1):
        size = index_to_size[i]
        first_loc = -1
        x = 0
        while x < len(disk) and first_loc == -1:
            start = x
            count = 0
            while x < len(disk) and disk[x] == '.' and count < size:
                count += 1
                x += 1
            if count >= size:
                first_loc = start
            x += 1

        if first_loc > -1 and first_loc < index_to_start[i]:
            for x in range(size):
                disk[index_to_start[i] + x] = '.'
            for x in range(size):
                disk[first_loc + x] = i

    x = 0
    for val in disk:
        if val != '.':
            result += val * x
        x += 1
    return result



if __name__ == '__main__':
    test = False

    input = open("test.txt", "r") if test else open("input.txt", "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))