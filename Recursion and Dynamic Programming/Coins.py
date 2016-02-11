def find_min_coins(target_change, coin_list, min_coins=[]):
    for change in range(target_change + 1):
        coin_count = change
        for j in [c for c in coin_list if c <= change]:
            if min_coins[change - j] + 1 < coin_count:
                coin_count = min_coins[change - j] + 1
        min_coins.append(coin_count)
    return min_coins[target_change]

def find_min_coin_combo(target_change, coin_list, min_coins=[]):
    for change in range(target_change + 1):
        min_num = change
        min_coin_dict = {k:0 for k in coin_list}
        for coin in [c for c in coin_list if c <= change]:
            if min_coins[change - coin][0] + 1 < min_num:
                min_num = min_coins[change - coin][0] + 1
                min_coin_dict = dict(min_coins[change - coin][1])
                min_coin_dict[coin] += 1
        min_coins.append((min_num, min_coin_dict))
    return min_coins[target_change][1]

coin_list = [1, 5, 10, 21]

def find_coin_combos(target_change, coin_list):
    if target_change < 0:
        return 0

    if target_change == 0:
        return 1

    ways = 0
    for coin in [c for c in coin_list if c <= target_change]:
        ways += find_coin_combos(target_change - coin, coin_list)

    return ways


print(find_min_coins(50, coin_list))