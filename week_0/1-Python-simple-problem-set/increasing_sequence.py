def is_increasing(seq):
	result = False
	if len(seq) == 1:
		return True
	else:
		for index in range(len(seq)-1):
			if seq[index] < seq[index+1]:
				result = True
			else:
				return False
	return result

def main():
	test = [[1,2,3,4,5],[1], [5,6,-10],[1,1,1,1]]
	for seq in test:
		print(is_increasing(seq))
if __name__ == "__main__":
	main()