import sys
from cat import cat_one

argv = sys.argv[1::]


def main():
    for arg in argv:
        cat_one(arg)

if __name__ == "__main__":
    main()
