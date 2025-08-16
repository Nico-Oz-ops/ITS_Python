'''
Tema: Liste e condizioni
Obiettivo: Ripassare cicli e condizioni con liste.

Nome dell’esercizio: somma_multipli_di_tre

Traccia:
Scrivi una funzione che, data una lista di numeri interi, ritorni la 
somma dei soli elementi che si trovano in posizione multipla di 3 (cioè indice 0, 3, 6, …)

Esempio: [5, 7, 8, 10, 3, 9, 2] → somma = 5 + 10 + 2 = 17.

Suggerimento: Ricorda che l’indice parte da 0.
'''

def somma_multipli_di_tre(numeri: list[int]) -> int:

    somma = 0
    for i in range(len(numeri)):
        if i % 3 == 0:
            somma += numeri[i]
    return somma

numeri = [5, 7, 8, 10, 3, 9, 2]
print(somma_multipli_di_tre(numeri))
