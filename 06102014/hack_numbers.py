from int_palindromes import is_int_palindrome
def next_hack(n):
    binary_n = bin(n)
    binary_n = binary_n[2::]
    center = len(binary_n) // 2


print(next_hack(1000))
