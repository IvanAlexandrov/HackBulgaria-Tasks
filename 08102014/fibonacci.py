
def nth_fibonacci(n):
    if n <= 2:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


def main():
    test = [0, 1, 2, 3, 10]
    for number in test:
        print(nth_fibonacci(number))

if __name__ == "__main__":
    main()
