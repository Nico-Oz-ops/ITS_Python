# Filtra e transforma e numeri

# Alternativa 1
def filter_and_square(nums: list[int], soglia: int) -> list[int]:
    return [num ** 2 for num in nums if num > soglia and num % 2 == 0]


# Alternativa 2
def filter_and_square(nums: list[int], soglia: int) -> list[int]:
    lista_nuova = []

    for num in nums:
        if num > soglia and num % 2 == 0:
            lista_nuova.append(num)
    return lista_nuova




