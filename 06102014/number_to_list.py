def number_to_list(n):
	n = str(n)
	result = []
	for digit in n:
		result.append(int(digit))

	return result

def main():
	test = [123, 99999, 123023]
	for number in test:
		print(number_to_list(number))

if __name__ == "__main__":
    main()
