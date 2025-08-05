'''
Tema: Ricorsione su lista
Obiettivo: Calcolare la somma degli elementi dispari in una lista di interi.
'''

# Esercizio 01
# Titolo: "somma_dispari"

'''
Traccia:
Scrivi una funzione ricorsiva che prende una lista di interi e 
restituisce la somma di tutti i numeri dispari presenti nella lista.

Suggerimento:
Controlla il primo elemento se è dispari, somma o salta, 
e poi richiama la funzione sul resto della lista.
'''

def somma_dispari(lista: list[int]) -> int:
    if len(lista) == 0:
        return 0
    
    elemento = lista[0]

    if elemento % 2 == 1:
        return elemento + somma_dispari(lista[1:])
    
    else:
        return somma_dispari(lista[1:])

print(somma_dispari([2, 4, 6, 8]))
print(somma_dispari([1, 3, 5, 7, 9]))
print(somma_dispari([1, 2, 3, 4, 5, 6, 7, 8, 9]))