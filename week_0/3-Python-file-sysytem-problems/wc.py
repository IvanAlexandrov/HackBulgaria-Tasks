import sys


def chars_counter(fp):
    # counter = 0
    content = fp.read()
    # content = content.split(" ")
    # for element in content:
    #     if (element.isalpha()):
    #         counter += len(element)
    #     else:
    #       continue
    # return counter
    return len(content)


def word_counter(fp):
    counter = 0
    content = fp.read()
    content = content.split()
    for element in content:
        if (element.isalpha()):
            counter += 1
        else:
            continue
    return counter


def line_counter(fp):
    counter = 0
    # content = content.split("\n")
    while fp.readline():
        counter += 1
    return counter


def main():
    fp = open(sys.argv[2], "r")
    # content = fp.read()
    if sys.argv[1] == 'chars':
        print(chars_counter(fp))
    elif sys.argv[1] == 'words':
        print(word_counter(fp))
    elif sys.argv[1] == 'lines':
        print(line_counter(fp))
    fp.close()

if __name__ == "__main__":
    main()
