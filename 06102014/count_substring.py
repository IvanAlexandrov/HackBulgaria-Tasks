
def count_substrings(haystack, needle):
    count = 0
    haystack = haystack.split()
    for element in haystack:
        if element == needle:
            count += 1

        if len(element) > len(needle):
            for sub_element in range(0, len(element), len(needle)):
                lenght = sub_element + len(needle)
                if element[sub_element:lenght] == needle:
                    count += 1
    return count

def main():
    print(count_substrings("This is a test string", "is"))
    print(count_substrings("babababa", "baba"))
    print(count_substrings("Python is an awesome language to program in!", "o"))
    print(count_substrings("We have nothing in common!", "really?"))
    print(count_substrings("This is this and that is this", "this"))

if __name__ == "__main__":
    main()