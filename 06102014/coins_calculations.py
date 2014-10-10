def calculate_coins(sum_):
    coins = [100, 50, 20, 10, 5, 2, 1]
    sum_ *= 100
    result = {1: 0, 2: 0, 100: 0, 5: 0, 10: 0, 50: 0, 20: 0}
    while sum_ > 0:
        for coin in coins:
            if sum_ - coin >= 0:
                if coin in result:
                    result[coin] += 1
                    sum_ -= coin
                    break
                else:
                    result[coin] = 1
                    sum_ -= coin
                    break
    return result
print(calculate_coins(0.53))
