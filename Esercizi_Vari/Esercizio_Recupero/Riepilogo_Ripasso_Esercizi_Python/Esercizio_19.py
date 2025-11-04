'''
Tema: Ordinamento di liste

Obiettivo: Ordinare manualmente una lista di numeri

Nome dell’esercizio: ordina_lista

Traccia:
Scrivi una funzione chiamata ordina_lista(lista_numeri) che riceve come parametro una 
lista di numeri interi o decimali non ordinata.

La funzione deve restituire una nuova lista contenente gli stessi numeri ordinati in 
ordine crescente (dal più piccolo al più grande).

Non puoi utilizzare funzioni o metodi built-in come sorted() o .sort().
Dovrai invece implementare un algoritmo di ordinamento manuale, come ad esempio Bubble Sort, 
Selection Sort o un approccio con confronti e scambi.

Se la lista è vuota, restituisci una lista vuota.

Esempio:

print(ordina_lista([5, 2, 9, 1, 7]))  # Output atteso: [1, 2, 5, 7, 9]
print(ordina_lista([]))               # Output atteso: []
'''

def ordina_lista(lista_numeri: list[int]) -> list[int]:
    lista_ordinata = lista_numeri[:]
    n = len(lista_numeri)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ordinata[j] > lista_ordinata[j + 1]:
                lista_ordinata[j + 1], lista_ordinata[j] = lista_ordinata[j], lista_ordinata[j + 1]

    if not lista_ordinata:
        return []
    
    return lista_ordinata

lista_numeri = [5, 2, 9, 1, 7]
list_num = []
print(ordina_lista(lista_numeri))
print(ordina_lista(list_num)) 
