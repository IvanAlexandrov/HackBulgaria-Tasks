from prime_number import is_prime


def goldbach(n):
    result = []
    primes_list = []
    for i in range(2, n):
        if is_prime(i):
            primes_list.append(i)
    count_primes = len(primes_list)
    center_of_prime_list = count_primes // 2
    left_part = primes_list[0:center_of_prime_list:1]
    right_part = primes_list[-1:center_of_prime_list-1:-1]
    for number_l in left_part:
        for number_r in right_part:
            if number_l + number_r == n:
                result.append((number_l, number_r))
                break
            elif number_l + number_r > n:
                pass
                # left_part.pop(number_l)
            else:
                pass
                # right_part.remove(number_r)
    return result

# print(goldbach(4))
# print(goldbach(6))
# print(goldbach(8))
# print(goldbach(10))
print(goldbach(100))
