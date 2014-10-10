def iterations_of_nan_expand(expanded):
	# count = expanded.count("Not a")
	# print(count)
	if expanded == '':
		return 0
	count = 0
	expanded = expanded.split()
	last_elemet = expanded.pop()
	if last_elemet == "NaN":
		first_word = ''
		second_word = ''
		for index in range(len(expanded)):
			if not expanded:
				break
			else:
				first_word = expanded.pop()
				second_word = expanded.pop()
				if second_word == "Not" and first_word == "a":
					count += 1
				else:
					return False
	else:
		return False
	return count

print(iterations_of_nan_expand(""))
print(iterations_of_nan_expand("Not a NaN"))
print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
print(iterations_of_nan_expand("Show these people!"))
print(iterations_of_nan_expand("F the Not a Not a Not a NaN"))