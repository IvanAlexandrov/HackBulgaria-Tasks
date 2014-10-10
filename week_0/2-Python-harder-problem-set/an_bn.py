def is_an_bn(word):
    if word == '':
        return True
    elif word.startswith('b'):
        return False
    else:
        count_a = word.count('a')
        count_b = word.count('b')
        if count_a != count_b:
            return False
        for i in range(0, count_a, 1):
            if 'b' in word[:count_a]:
                return False
            else:
                return True


print(is_an_bn(""))
print(is_an_bn("rado"))
print(is_an_bn("aaabb"))
print(is_an_bn("aaabbb"))
print(is_an_bn("aabbaabb"))
print(is_an_bn("bbbaaa"))
print(is_an_bn("aaaaabbbbb"))
