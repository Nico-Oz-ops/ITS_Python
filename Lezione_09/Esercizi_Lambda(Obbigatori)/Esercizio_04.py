# Esercizio 04
'''
Ordinamento con sorted()
Hai una lista di tuple studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)]. 
Ordina la lista in base all’età (secondo elemento) usando sorted() e lambda.
'''

from typing import Callable

studenti = [("Luca", 21), ("Anna", 19), ("Marco", 22)]

sorted_età:Callable[[str, int], int] = sorted(studenti, key=lambda età: età[1])
print(sorted_età)

from typing import Callable

studenti = [("Luca", 21), ("Susanna", 19), ("Marco", 22)]

sorted_nome = sorted(studenti, key=lambda nome: nome[0])
print(sorted_nome)