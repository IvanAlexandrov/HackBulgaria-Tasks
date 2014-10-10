from int_palindromes import is_int_palindrome


def next_hack(n):
    n <<= 1
    print(n)
    binary_n = bin(n)
    binary_n = binary_n[2:]
    ones = binary_n.count("1")
    # print(is_int_palindrome(int(binary_n)), ones)
    if is_int_palindrome(int(binary_n)) and ones % 2 != 0:
        return n
    return next_hack(n + 1)


print(next_hack(0))
print(next_hack(10))
print(next_hack(8031))
print(next_hack(1000))
