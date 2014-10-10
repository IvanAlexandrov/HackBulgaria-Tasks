import sys
from random import randint


def main():
    if len(sys.argv) < 3:
        print(
            "Usage:\n"
            "1-st parameter is [filename]\n"
            "2-nd parameter is [number of radoms]"
        )
        exit()
    filename = sys.argv[1]
    numbers = int(sys.argv[2])
    fp = open(filename, "w")
    for i in range(0, numbers):
        fp.write(str(randint(1, 1000)) + " ")
    fp.close()

if __name__ == '__main__':
    main()
