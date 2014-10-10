from list_to_number import list_to_number
def zero_insert(n):
    n = str(n)
    result = []
    if len(n) == 1:
        return int(n)
    else:
        for digit1, digit2 in zip(range(0, len(n)-1, 2), range(1, len(n), 2)):
            if n[digit1] == n[digit1-1]:
                result.append(0)
            if n[digit1] == n[digit2] or (int(n[digit1]) + int(n[digit2])) % 10 == 0:
                result.append(int(n[digit1]))
                result.append(0)
                result.append(int(n[digit2]))
            else:
                result.append(int(n[digit1]))
                result.append(int(n[digit2]))

    return list_to_number(result)

def main():
    test = [116457, 555555555, 1, 6446]
    for number in test:
        print(zero_insert(number))

if __name__ == "__main__":
    main()
505050505050505