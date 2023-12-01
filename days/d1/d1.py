import re


def pt1():
    total_sum = 0
    for x in lines:
        num_only = re.sub("[a-z]", "", x)
        total_sum += (int(num_only[0] + num_only[-1]))
    return total_sum


def pt2():
    replace_list = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                    "eight": "8", "nine": "9", "threeight": "3", "fiveight": "5", "sevenine": "7",
                    "eightwo": "8", "eighthree": "8", "nineight": "9"}
    combo_replace = {"oneight": "oneeight", "twone": "twoone", "threeight": "threeeight", "fiveight": "fiveeight",
                     "sevenine": "sevennine",
                     "eightwo": "eighttwo", "eighthree": "eightthree", "nineight": "nineeight"}
    total_sum = 0
    for x in lines:
        for key, value in combo_replace.items():
            x = x.replace(key, value)
        for key, value in replace_list.items():
            x = x.replace(key, value)
        num_only = re.sub("[a-z]", "", x)
        total_sum += (int(num_only[0] + num_only[-1]))
    return total_sum


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    print("part1: " + str(pt1()))
    print("part2: " + str(pt2()))
