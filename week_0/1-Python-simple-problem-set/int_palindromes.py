def is_int_palindrome(n):
    n = str(n)
    reversed_n = n[-1::-1]
    if n == reversed_n:
        return True
    else:
        return False


def main():
    test = [1, 42, 100001, 999, 123, 123321, 1221]
    for n in test:
        print(is_int_palindrome(n))

if __name__ == "__main__":
    main()
