import re


def pt1():
    lines_detail = [[(".", False) for x in range(len(lines[0]))] for y in range(len(lines))]
    match_number = re.compile(r"\d")
    match_symbol = re.compile(r"[^\d.]")
    for current_y in range(0, len(lines)):
        for current_x in range(0, len(lines[0])):
            if match_number.match(lines[current_y][current_x]) is not None:
                for add_y in range(-1, 2):
                    for add_x in range(-1, 2):
                        if len(lines) > current_y + add_y >= 0 and len(lines[0]) > current_x + add_x >= 0:
                            test_cell = lines[current_y + add_y][current_x + add_x]
                            if match_symbol.match(test_cell) is not None:
                                lines_detail[current_y][current_x] = (lines[current_y][current_x], True)
                            else:
                                lines_detail[current_y][current_x] = (lines[current_y][current_x], lines_detail[current_y][current_x][1])
    # by this point, lines detail contains the digits and if each digit has a symbol adjacent
    part_numbers = []
    for current_y in range(0, len(lines)):
        for current_x in range(0, len(lines[0])):
            if match_number.match(lines_detail[current_y][current_x][0]) is not None:
                is_symbol_adjacent = lines_detail[current_y][current_x][1]
                merged_digits = lines_detail[current_y][current_x][0]
                for next_cell in range(current_x+1, len(lines[0])):
                    if match_number.match(lines_detail[current_y][next_cell][0]) is not None:
                        merged_digits = merged_digits + lines_detail[current_y][next_cell][0]
                        if lines_detail[current_y][next_cell][1]:
                            is_symbol_adjacent = True
                        lines_detail[current_y][next_cell] = (".", False)
                    else:
                        break
                part_numbers.append((merged_digits, is_symbol_adjacent))

    sum_total = 0
    for part_number in part_numbers:
        if part_number[1] is True:
            sum_total += int(part_number[0])
    return sum_total


def pt2():
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    print("part1: " + str(pt1()))
    print("part2: " + str(pt2()))
