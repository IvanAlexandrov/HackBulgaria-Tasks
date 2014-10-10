def contains_digits(number, digits):
    if len(digits) == 0:
        return True
    else:
        result = []
        number = str(number)
        for i in number:
            if int(i) in digits:
                result.append(True)
        if len(result) == len(digits):
            return True
        else:
            return False


def main():
    print(contains_digits(402123, [0, 3, 4]))
    print(contains_digits(666, [6,4]))
    print(contains_digits(123456789, [1,2,3,0]))
    print(contains_digits(456, []))

if __name__ == "__main__":
    main()