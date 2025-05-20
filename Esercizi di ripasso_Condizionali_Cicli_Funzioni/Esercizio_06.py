# Esercizio 6

def sum_above_threshold(numbers:list[int], num=20) -> int:

    result = 0

    for i in numbers:
        if i > num:
            result += i
    return result

print(sum_above_threshold([15, 5, 25], 10))


