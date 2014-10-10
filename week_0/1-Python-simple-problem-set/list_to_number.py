def list_to_number(digits):
	
	result = ''
	for digit in digits:
		result += str(digit)

	return int(result)

def main():
	test = [[1,2,3], [9,9,9,9,9], [1,2,3,0,2,3]]
	for digits in test:
		print(list_to_number(digits))

if __name__ == "__main__":
    main()
