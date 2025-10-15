def filter_and_concat(nums: list[int], min_val: int) -> str:
    filtro = ", ".join(str(num) for num in nums if num > min_val)

    return filtro

numbers = [1, 5, 7, 6, 3, 5]
min_value = 4
print(filter_and_concat(numbers, min_value))

def filter_and_concat(nums: list[int], min_val: int) -> str:
    nuova_lista = []
    for num in nums:
        if num > min_val:
            nuova_lista.append(str(num))

    stringa = ', '.join(nuova_lista)
    return stringa

numbers = [1, 5, 7, 6, 3, 5]
min_value = 4
print(filter_and_concat(numbers, min_value))

