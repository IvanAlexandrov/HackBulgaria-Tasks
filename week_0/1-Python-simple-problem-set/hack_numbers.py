from int_palindromes import is_int_palindrome


def next_hack(n):
    n += 1
    binary_n = bin(n)
    binary_n = binary_n[2:]
    ones = binary_n.count("1")
    if is_int_palindrome(binary_n) and ones % 2 != 0:
        print(n)
        return n
    next_hack(n)

print(next_hack(0))
print(next_hack(10))
print(next_hack(8031))
print(next_hack(1000))
