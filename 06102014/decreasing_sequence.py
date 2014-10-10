def is_decreasing(seq):
    print(seq)
    result = False
    if len(seq) == 1:
        return False
    else:
        for index in range(len(seq)-1):
            if seq[index] > seq[index+1]:
                result = True
            else:
                return False
    return result

def main():
    test = [[5,4,3,2,1], [1,2,3], [100, 50, 20],[1,1,1,1]]
    for seq in test:
        print(is_decreasing(seq))
if __name__ == "__main__":
    main()