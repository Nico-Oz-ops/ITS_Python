def dedup_stable(nums: list[int]) -> list[int]:

    if not nums:
        return []

    list_nuova = [nums[0]]
    n = len(nums)

    for i in range(1, n):
        if nums[i] != nums[i-1]:
            list_nuova.append(nums[i])
    
    return list_nuova


nums = [1, 2, 2, 3, 8, 6, 7, 6]
print(dedup_stable(nums))



# Versione 2
def dedup_stable(nums: list[int]) -> list[int]:
    visti = set()
    lista_nuova = []

    for num in nums:
        if num not in lista_nuova:
            lista_nuova.append(num)
            visti.add(num)
    
    return lista_nuova
nums = [1, 2, 2, 3, 8, 6, 7, 6]
print(dedup_stable(nums))
