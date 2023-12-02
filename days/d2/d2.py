import re


def d2common():
    dct_store = {}
    for x in lines:
        parts_2 = x.split(":")
        game_no = parts_2[0].split(" ")[1]
        color_dict = {}
        for show in re.split('; |,', parts_2[1]):
            show = show.strip()
            color = show.split(" ")[1]
            number = int(show.split(" ")[0])
            if color in color_dict:
                if number > color_dict[color]:
                    color_dict[color] = number
            else:
                color_dict[color] = number
        dct_store[game_no] = color_dict
    return dct_store


def pt1():
    dct_store = d2common()
    sum_total = 0
    for game, result in dct_store.items():
        if result["red"] <= 12 and result["green"] <= 13 and result["blue"] <= 14:
            sum_total += int(game)
    return sum_total


def pt2():
    dct_store = d2common()
    sum_total = 0
    for game, result in dct_store.items():
        sum_total += (result["red"]*result["green"]*result["blue"])
    return sum_total


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    print("part1: " + str(pt1()))
    print("part2: " + str(pt2()))
