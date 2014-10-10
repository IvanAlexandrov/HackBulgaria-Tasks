def is_int_palindrome(n):
	n = str(n)
	if len(n) % 2 != 0 and len(n) < 4:
		return False
	center = len(n)//2
	first_part = n[0:center:1]
	second_part = n[-1:center-1:-1]
	if first_part == second_part:
		return True
	else:
		return False


def main():
	test = [1, 42, 100001, 999, 123, 123321, 1221]
	for n in test:
		print(is_int_palindrome(n))

if __name__ == "__main__":
	main()