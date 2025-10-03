'''
Evocalo con `symdiff_sorted(a, b)`, restituendo la lista **ordinata** degli 
interi che compaiono esattamente in una delle liste. 
'''

def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:
    return sorted(set(a) ^ set(b))  # ^ è l'operatore di differenza simmetrica

a = [1, 8, 5, 4]
b = [5, 6, 2, 3]
print(symdiff_sorted(a, b))