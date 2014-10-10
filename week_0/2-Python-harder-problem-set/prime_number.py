def is_prime(n):
    result = True
    if n <= 1:
        result = False
    else:
        # TODO optimize for large numbers

        divisor_limit = int(n ** 0.5)
        for i in range(2, divisor_limit + 1, 1):
            if n % i == 0:
                result = False
                break
        return result


def main():
    # 2 ** 57885161 - 1
    test = [1, 2, 8, 11, -10, 7, 17, 4]
    for number in test:
        print(is_prime(number))

if __name__ == "__main__":
    main()
