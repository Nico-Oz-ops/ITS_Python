'''
Tema: Ricerca di un valore in una lista

Obiettivo: Verificare la presenza di un elemento all’interno di una lista di numeri interi.

Nome dell’esercizio: trova_valore

Traccia:
Scrivi una funzione chiamata trova_valore(lista_numeri, valore) che prenda in input:

una lista di numeri interi (non necessariamente ordinata)

un valore intero da cercare nella lista

La funzione deve restituire True se il valore è presente nella lista, altrimenti False.
Non utilizzare la parola chiave in: implementa la ricerca manualmente, iterando sugli elementi della lista.

Suggerimento:
Puoi scorrere la lista con un ciclo for e confrontare ogni elemento con il valore cercato. 
Se trovi una corrispondenza, restituisci subito True. Se il ciclo termina senza trovarlo, restituisci False.
'''
def trova_valore(lista_numeri: list[int], valore: int) -> bool:

    # scorre la lista
    for numero in lista_numeri:
        if numero == valore:
            return True
    # Se il ciclo termina senza trovare il valore, restituisce False 
    return False

print(trova_valore([3, 7, 1, 9, 4], 9)) 
print(trova_valore([3, 7, 1, 9, 4], 5)) 