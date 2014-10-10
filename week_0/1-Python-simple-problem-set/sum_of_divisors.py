def sum_of_divisors(n):
	result = 0
	for i in range(1, n+1, 1):
		if n % i == 0:
			result += i
	return result

def main():
	test = [8, 7, 1, 1000, 0, 10]
	for number in test:
		print(sum_of_divisors(number))

if __name__ == "__main__":
	main()
