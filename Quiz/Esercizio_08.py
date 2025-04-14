# Esercizio 8

def count_isolated(lista: list[int]) -> int:
    count = 0

    for i in range(len(lista)): # verifico per ogni elemento della lista

        # controllo se l'elemento è isolato
        if (i == 0 or lista[i] != lista[i - 1]) and (i == len(lista) - 1 or lista[i] != lista[i + 1]):
            count += 1
            
    return count

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))