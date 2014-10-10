import sys


def main():
    if len(sys.argv) < 2:
        print(
            "Usage:\n"
            "1-st parameter is [filename]\n"
        )
        exit()
    filename = sys.argv[1]
    fp = open(filename, "r")
    contents = fp.read()
    fp.close()
    contents_list = contents.split(" ")
    sum_of_ints = 0
    for number in contents_list:
        if number != '':
            sum_of_ints += int(number)
        else:
            continue
    print(sum_of_ints)

if __name__ == '__main__':
    main()
