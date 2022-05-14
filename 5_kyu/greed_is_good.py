from collections import Counter


def score(dice):
    total = 0
    triplets = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
    for num, points in Counter(dice).items():
        if points >= 3:
            total += triplets[num] * (points // 3)
        if num == 1:
            total += 100 * (points % 3)
        elif num == 5:
            total += 50 * (points % 3)
    return total
