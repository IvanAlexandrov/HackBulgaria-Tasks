import math
def sum_of_digits(n):
	n = abs(n)
	n = str(n)
	result = 0
	for number in n:
		result += int(number)
	return result

def main():
	tests  = [1325132435356, 123, 6, -10, -33,  -4213, 87429510488]
	for number in tests:
		print(sum_of_digits(number))

if __name__ == "__main__":
	main()