import sys
argv = sys.argv


def cat_one(file_name):
    if file_name == '':
        file_name = argv[1]
    fp = open(file_name, "r")
    print(file.read())
    fp.close()


def main():
    if len(argv) == 1:
        pass
    else:
        cat_one(argv[1])

if __name__ == '__main__':
    main()
