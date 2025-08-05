'''
Tema: Ricorsione su liste
Obiettivo: Sommare ricorsivamente gli elementi di una lista di interi.
'''

# Esercizio 05
# Titolo: "Somma lista interi"

'''
Traccia:
Scrivi una funzione ricorsiva somma_lista che prende in input 
una lista di numeri interi e restituisce la somma di tutti gli elementi.

Suggerimento (se serve):
Pensa alla prima posizione della lista, e fai una chiamata ricorsiva sul resto della lista (lista[1:]).
'''

def somma_lista(lista_num:list[int]) -> int:

    if len(lista_num) == 0:
        return  0
    
    else:
        return lista_num[0] + somma_lista(lista_num[1:])

print(somma_lista([1, 2, 3, -5, 10]))

    