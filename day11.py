"""
cadybaltz
12/11/2024
AoC 2024 Day 11
Part 1: 3335, 00:12:52
Part 2: 1969, 00:25:57
"""

def remove_leading_zero(val):
    val_list = list(val)
    x = 0
    while x < len(val_list) and val_list[x] == '0':
        x += 1

    result = ''
    while x < len(val_list):
        result = result + val_list[x]
        x += 1
    if len(result) == 0:
        result = '0'
    return result

def split_even_val(val):
    mid = (len(val) + 1) // 2
    return remove_leading_zero(val[:mid]), remove_leading_zero(val[mid:])

def pt_1_solution(lines):
    for line in lines:
        vals = line.split()
        for _ in range(25):

            new_vals = []
            for x in range(len(vals)):
                if vals[x] == '0':
                    new_vals.append('1')
                elif len(vals[x]) % 2 == 0:
                    split1, split2 = split_even_val(vals[x])
                    new_vals.append(split1)
                    new_vals.append(split2)
                else:
                    new_vals.append(str(int(vals[x]) * 2024))
            vals = new_vals.copy()
    return len(vals)

memo = {}
def rec(val, rem):
    if (val,rem) in memo:
        return memo[(val,rem)]
    elif rem == 0:
        if len(val) % 2 == 0:
            memo[(val,rem)] = 2
            return 2
        else:
            memo[(val, rem)] = 1
            return 1
    else:
        if val == '0':
            result = rec('1', rem-1)
            memo[(val, rem)] = result
            return result
        elif len(val) % 2 == 0:
            split1, split2 = split_even_val(val)
            result = rec(split1, rem-1) + rec(split2,rem-1)
            memo[(val, rem)] = result
            return result
        else:
            result = rec(str(int(val) * 2024), rem - 1)
            memo[(val, rem)] = result
            return result

def pt_2_solution(lines):
    result = 0
    for line in lines:
        vals = line.split()
        for x in range(len(vals)):
            result += rec(vals[x], 74)

    return result



if __name__ == '__main__':
    test = False

    input = open("test.txt", "r") if test else open("input.txt", "r")

    lines = input.readlines()
    print("Part 1: " + str(pt_1_solution(lines)))
    print("Part 2: " + str(pt_2_solution(lines)))