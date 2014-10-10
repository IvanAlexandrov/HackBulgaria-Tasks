def count_consonants(str):
    consonants = 'bcdfghjklmnpqrstvwxz'
    consonants += consonants.upper()
    count = 0
    for character in str:
        if character in consonants:
            count += 1
    return count

def main():
    test = ["Python", 
        "Theistareykjarbunga",
        "grrrrgh!",
         "Github is the second best thing that happend to programmers, after the keyboard!",
         "A nice day to code!"
         ]
    for str in test:
        print(count_consonants(str))

if __name__ == "__main__":
    main()
