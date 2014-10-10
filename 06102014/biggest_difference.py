def biggest_difference(arr):
    min_value = min(arr)
    max_value = max(arr)
    return min_value - max_value

def main():
    test = [[1,2], [1,2,3,4,5], [-10, -9, -1],range(100)]
    for lists in test:
        print(biggest_difference(lists))

if __name__ == "__main__":
    main()
