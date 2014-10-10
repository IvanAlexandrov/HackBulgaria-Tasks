from prime_number import is_prime


def prime_factorization(n):
    result = []
    while n > 1:
        for index in range(2, n+1):
            if is_prime(index):
                counter = 0
                while n % index == 0:
                    counter += 1
                    n = n / index
                    if counter > 1:
                        result.append((index, counter + 1))
    return result


print(prime_factorization(10))
print(prime_factorization(14))
print(prime_factorization(356))
print(prime_factorization(89))
print(prime_factorization(1000))
