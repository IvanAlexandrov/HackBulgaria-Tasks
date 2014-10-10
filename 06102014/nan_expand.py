def nan_expand(times):
    if times == 0:
        return "\"\""
    else:
        return "\"" + "Not a " * times + "NaN\""

def main():
    test = [0, 1, 2, 3]
    for number in test:
        print(nan_expand(number))
if __name__ == "__main__":
    main()