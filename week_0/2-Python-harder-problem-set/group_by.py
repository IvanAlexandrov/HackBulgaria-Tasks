def groupby(func, seq):
    result = {}
    for element in seq:
        key = func(element)
        new_seq = []
        new_seq.append(element)
        if key not in result:
            result[key] = new_seq
        else:
            result[key].append(new_seq[0])
    print(result)

groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7])
groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12])
groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7])
