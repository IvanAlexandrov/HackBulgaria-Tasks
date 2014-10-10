def is_number_balanced(n):
    n = str(n)
    if len(n) == 1:
        return True
    else:
        left_sum = 0
        right_sum = 0
        center = len(n) // 2
        if len(n) % 2 != 0:
            left_part = n[:center]
            right_part = n[center+1:]
            for i in left_part:
                left_sum += int(i)
            for i in right_part:
                right_sum += int(i)
            if left_sum == right_sum:
                return True
            else:
                return False
        else:
            left_part = n[:center]
            right_part = n[center:]
            for i in left_part:
                left_sum += int(i)
            for i in right_part:
                right_sum += int(i)
            if left_sum == right_sum:
                return True
            else:
                return False


def main():
    test = [9, 11, 13, 121, 4518, 28471, 1238033]
    for n in test:
        print(is_number_balanced(n))

if __name__ == "__main__":
    main()