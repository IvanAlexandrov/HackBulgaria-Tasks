def prepare_meal(number):
    if number == 0:
        return ""
    result = ''
    if number % 5 == 0:
        if number % 3 != 0:
            result = 'eggs'
        else:
            result += 'and eggs'
    while number % 3 == 0:
        result = 'spam ' + result
        number /= 3
    return result.rstrip()
print(prepare_meal(3))
print(prepare_meal(27))
print(prepare_meal(7))
print(prepare_meal(5))
print(prepare_meal(15))
print(prepare_meal(45))
