'''
Tema: Collezioni e funzioni funzionali (set, any, filter, lambda).
Obiettivo: Verificare se una lista contiene elementi duplicati, evitando cicli for espliciti e utilizzando strumenti funzionali.

Nome dell’esercizio: contiene_duplicati

Traccia:
Scrivi una funzione contiene_duplicati(lista) che restituisce True se la 
lista contiene almeno un elemento duplicato, altrimenti False.

La funzione deve evitare l’uso di cicli for espliciti e deve invece 
usare strumenti come set, any, lambda, filter.

Suggerimento: 
Puoi confrontare la lunghezza della lista con la lunghezza dell'insieme degli elementi unici. 
Oppure, puoi usare any() e accumulare dinamicamente gli elementi già visti in un set.
'''
from typing import Any

def contiene_duplicati(elementi: list[Any]) -> bool:
    elementi_visti = set()
    return any(filter(lambda elemento: elemento in elementi_visti or elementi_visti.add(elemento), elementi))


print(contiene_duplicati([1, 2, 3, 4]))        
print(contiene_duplicati([1, 2, 3, 1]))         
print(contiene_duplicati(["a", "b", "a"]))      
print(contiene_duplicati(["a", "b", "c"]))  