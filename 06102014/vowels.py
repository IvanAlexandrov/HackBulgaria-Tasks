def count_vowels(str):
	vowels = "aeiouy"
	vowels += vowels.upper()
	count = 0
	for character in str:
		if character in vowels:
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
		print(count_vowels(str))

if __name__ == "__main__":
	main()

