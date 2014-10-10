import sys
argv = sys.argv[1::]

def main():
    output_file = open("./test_files/MEGATRON", "a+")

    for arg in argv:
        file_reader = open(arg, "r")
        output_file.write(file_reader.read() + "\n")
        file_reader.close()
    output_file.close()
if __name__ == "__main__":
    main()
