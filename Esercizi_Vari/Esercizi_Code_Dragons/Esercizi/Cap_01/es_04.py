'''
Suddividi la sequenza con `chunk(lst, size)`, spezzando `lst` in sottoliste 
consecutive di lunghezza `size` (l'ultimo blocco può essere più corto).
'''

def chunk(lst: list[int], size: int) -> list[list[int]]:
    return [lst[i:i + size] for i in range(0, len(lst), size)]

lst = [1, 2 ,3, 4, 5, 6, 7, 8, 9]
print(chunk(lst, 2))

