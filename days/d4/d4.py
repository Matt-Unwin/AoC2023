def d4_read():
    dct_store = {}
    for x in lines:
        parts_2 = x.split(":")
        game_no = parts_2[0].split()[1].strip()

        winning_numbers = parts_2[1].split("|")[0].strip().split()
        chosen_numbers = parts_2[1].split("|")[1].strip().split()

        dct_store[game_no] = (winning_numbers, chosen_numbers)
    return dct_store


def pt1():
    dct_store = d4_read()
    sum_total = 0
    for game, (winning_numbers, chosen_numbers) in dct_store.items():
        card_points = 0
        for chosen_number in chosen_numbers:
            if chosen_number in winning_numbers:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points *= 2
        sum_total += card_points
    return sum_total


def pt2():
    dct_store = d4_read()
    new_dct = {}

    for game, (winning_numbers, chosen_numbers) in dct_store.items():
        card_points = 0
        for chosen_number in chosen_numbers:
            if chosen_number in winning_numbers:
                card_points += 1
        new_dct[int(game)] = (card_points, 1)

    for game, (original_score, multiplier) in new_dct.items():
        for addition in range(1, original_score + 1):
            new_dct[int(game) + addition] = (
                new_dct[int(game) + addition][0], new_dct[int(game) + addition][1] + multiplier)

    sum_total = 0
    for game, (original_score, multiplier) in new_dct.items():
        sum_total += multiplier
    return sum_total


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
    print("part1: " + str(pt1()))
    print("part2: " + str(pt2()))
