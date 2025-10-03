'''
Invoca `intersection_sorted(a, b)` per restituire la lista **ordinata** degli interi 
presenti sia in `a` sia in `b`, senza duplicati.
'''

def intersection_sorted(a: list[int], b: list[int]) -> list[int]:
    return list(sorted(set(a) & set(b)))

a = [1, 8, 5, 4, 4]
b = [5, 6, 2, 3, 5]
print(intersection_sorted(a,b))