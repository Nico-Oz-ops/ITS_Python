'''
Realizza l'intreccio con `flatten_once(nested)`, che appiattisce di un 
livello una lista di liste concatenando le sottoliste
'''
# Versione 1
def flatten_once(nested: list[list[int]]) -> list[int]:
    return [elemento for sottolista in nested for elemento in sottolista]


# Versione 2
nested = [[1, 2], [3, 4], [5, 6], [7, 8], [9]]
print(flatten_once(nested))

def flatten_once(nested: list[list[int]]) -> list[int]:
    nuova_lista = []

    for sottolista in nested:
        for elemento in sottolista:
            if elemento not in nuova_lista:
                nuova_lista.append(elemento)
    
    return nuova_lista

nested = [[1, 2], [3, 4], [5, 6], [7, 8], [9]]
print(flatten_once(nested))

