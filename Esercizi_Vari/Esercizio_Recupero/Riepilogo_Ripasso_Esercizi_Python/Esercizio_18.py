'''
Tema: Liste e cicli

Obiettivo: Calcolare manualmente il minimo e il massimo di una lista

Nome dell’esercizio: trova_min_max

Traccia:
Scrivi una funzione chiamata trova_min_max(lista_numeri) che prende in input una lista di numeri interi o decimali non ordinata.
La funzione deve restituire una tupla contenente due elementi:

Il valore minimo nella lista.

Il valore massimo nella lista.

Non puoi utilizzare le funzioni built-in min() e max().
Dovrai invece determinare i valori minimo e massimo scorrendo la lista con un ciclo.

Se la lista è vuota, la funzione deve restituire None.

Esempio:

print(trova_min_max([7, 3, 9, 1, 5]))  # Output atteso: (1, 9)
print(trova_min_max([]))               # Output atteso: None


Suggerimento:
Inizializza due variabili, minimo e massimo, con il primo elemento della lista, poi aggiornale confrontando ciascun valore successivo nel ciclo.
'''