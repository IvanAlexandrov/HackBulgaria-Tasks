from prime_number import is_prime

def prime_number_of_divisors(n):
	number_of_divisors = 0
	for i in range(1, n + 1, 1):
		if n % i == 0:
			number_of_divisors += 1
	print(number_of_divisors)

	if is_prime(number_of_divisors):
		return True
	else:
		return False

def main():
	test = [7, 8, 9, 10, 12, 0]
	for number in test:
		print(prime_number_of_divisors(number))

if __name__ == "__main__":
	main()

