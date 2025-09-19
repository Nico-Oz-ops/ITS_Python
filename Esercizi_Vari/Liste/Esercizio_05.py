'''
Esercizio 5

Tema: Liste annidate e trasformazioni
Obiettivo: Allenarsi a filtrare e trasformare elementi in liste di liste

Nome dell’esercizio: Doppio filtro e moltiplicazione

Traccia:

Hai una lista di liste di numeri, ad esempio:
numeri = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Scrivi una funzione filtra_e_moltiplica(liste, n) che:

    1. Filtri solo i numeri maggiori di n in ogni sotto-lista.
    2. Moltiplichi per 2 ogni numero filtrato.

Esempio:

filtra_e_moltiplica(numeri, 4)
# Output: [[ ], [5*2, 6*2], [7*2, 8*2, 9*2]]
# Risultato: [[], [10, 12], [14, 16, 18]]
'''
# Alternativa 1
def filtra_e_moltiplica(numeri: list[list[int]], n: int):
    return [[numero * 2 for numero in numeri_annidati if numero > n] for numeri_annidati in numeri]

numeri = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = 2

print(filtra_e_moltiplica(numeri, n))

# Alternativa 2
def filtra_e_moltiplica(numeri: list[list[int]], n: int):
    risultato = []

    for lista_annidata in numeri:
        filtro = []
        for numero in lista_annidata:
            if numero > n:
                filtro.append(numero * 2)
        
        risultato.append(filtro)
    
    return risultato

numeri = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = 4

print(filtra_e_moltiplica(numeri, n))


# Alternativa 3
def filtra_e_moltiplica(numeri: list[list[int]], n: int):
    return list(map(lambda lista: list(map(lambda numero: numero * 2, filter(lambda numero: numero > n, lista))), numeri))


numeri = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = 4

print(filtra_e_moltiplica(numeri, n))


'''
** Come funziona **

map(..., numeri) → prende ogni sotto-lista dentro numeri.

Dentro la lambda lista:

filter(lambda x: x > n, lista) → tiene solo i numeri maggiori di n.

map(lambda x: x * 2, ...) → raddoppia ogni numero filtrato.

list(...) → converte il risultato in lista.

Alla fine, un altro list(...) esterno raccoglie tutte le sotto-liste trasformate.
'''