from prime_number import is_prime


def goldbach(n):
    result = []
    primes_list = []
    for i in range(2, n):
        if is_prime(i):
            primes_list.append(i)
    count_primes = len(primes_list)
    center = count_primes // 2
    # left_part = primes_list[0:center:1]
    # right_part = primes_list[-1:center-1:-1]
    # print(left_part, right_part)
    i = len(primes_list) -1
    j = 0
    while (i >= 0):
        print(i, j)
        # print(primes_list[i], primes_list[j])
        left_part = primes_list[j]
        right_part = primes_list[i]
        if (left_part + right_part > n):
            pass
            # left_part = primes_list[j + 1]
        elif (left_part + right_part < n):
            pass
            # right_part = primes_list[i - 1]
        elif(left_part + right_part == n):
            result.append((left_part, right_part))
            break
        i -= 1
        j += 1
    return result

print(goldbach(4))
print(goldbach(6))
# print(goldbach(8))
# print(goldbach(10))
print(goldbach(100))
