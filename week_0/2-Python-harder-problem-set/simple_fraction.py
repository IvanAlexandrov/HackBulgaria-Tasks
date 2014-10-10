def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    result = ()
    if nominator == 1:
        result = (nominator, denominator)
    else:
        if denominator % nominator == 0:
            denominator = denominator // nominator
            nominator = 1
        else:
            for i in range(2, denominator, 1):
                if nominator % i == 0 and nominator > 1:
                    if denominator % i == 0 and denominator > nominator:
                        nominator = nominator // i
                        denominator = denominator // i
                else:
                    nominator = nominator
                    denominator = denominator

        result = (nominator, denominator)
    return result

print(simplify_fraction((3, 9)))
print(simplify_fraction((1, 7)))
print(simplify_fraction((4, 10)))
print(simplify_fraction((63, 462)))
