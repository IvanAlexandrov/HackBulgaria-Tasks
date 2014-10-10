def contains_digit(number, digit):
    number = str(number)
    digit = str(digit)
    if number.find(digit) == True:
        return True
    else:
        return False

def main():
    print(contains_digit(123, 4))
    print(contains_digit(42, 2))
    print(contains_digit(1000, 0))
    print(contains_digit(12346789, 5))

if __name__ == "__main__":
    main()