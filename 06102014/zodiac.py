def what_is_my_sign(day, month):
    signs = {
        1: ["Aqiuaris", 21, 31],
        2: ["Pisces", 20, 29],
        3: ["Aries", 21, 31],
        4: ["Taurus", 21, 30],
        5: ["Gemini", 22, 31],
        6: ["Cancer", 21, 30],
        7: ["Leo", 23, 31],
        8: ["Virgo", 24, 31],
        9: ["Libra", 24, 30],
        10: ["Scorpio", 24, 31],
        11: ["Sagittarius", 23, 30],
        12: ["Capricorn", 22, 31],
    }
    sign = ''
    sign_guess = signs.get(month)
    if day >= sign_guess[1] and day <= sign_guess[2]:
        return sign_guess[0]
    elif month == 1 and day < sign_guess[1]:
        sign = signs.get(month + 11)
        return sign[0]
    elif month <= 12 and day < sign_guess[1]:
        sign = signs.get(month - 1)
    elif day < sign_guess[1]:
        sign = signs.get(month + 1)
    return sign[0]


# Tests
print(what_is_my_sign(7, 2))
print(what_is_my_sign(24, 7))
print(what_is_my_sign(29, 12))
print(what_is_my_sign(24, 9))

print()
print(what_is_my_sign(1, 1))
print(what_is_my_sign(5, 8))
print(what_is_my_sign(29, 1))
print(what_is_my_sign(30, 6))
print(what_is_my_sign(31, 5))
print(what_is_my_sign(2, 2))
print(what_is_my_sign(8, 5))
print(what_is_my_sign(9, 1))
print(what_is_my_sign(1, 12))
