def nth_fib_lists(listA, listB, n):
    new_list = []
    if n == 1:
        new_list = listA
    elif n == 2:
        new_list = listB
    elif n == 3:
        new_list = listA + listB
    else:
        for i in range(3, n + 1):
            new_list += listA + listB
    return new_list

print(nth_fib_lists([1], [2], 1))
[1]
print(nth_fib_lists([1], [2], 2))
[2]
print(nth_fib_lists([1, 2], [1, 3], 3))
[1, 2, 1, 3]
print(nth_fib_lists([], [1, 2, 3], 4))
[1, 2, 3, 1, 2, 3]
print(nth_fib_lists([], [], 100))
