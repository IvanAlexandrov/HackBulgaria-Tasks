from prime_number import is_prime


def goldbach(n):
    result = []
    primes_list = []
    for number in range(2, n // 2 + 1):
        if is_prime(number) and is_prime(n - number):
            result.append((number, n - number))
    return result

print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))
