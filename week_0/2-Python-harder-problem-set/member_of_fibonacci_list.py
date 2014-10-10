def member_of_nth_fib_lists(listA, listB, needle):
    new_list = listA + listB
    list_count = len(new_list)
    for n in range(0, len(needle)):
        needle_part = needle[n:list_count]
        if needle_part == new_list:
            return True
    return False


print(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
print(member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
print(member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))
print(member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))
