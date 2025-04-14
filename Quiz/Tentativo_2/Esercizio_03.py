# Esercizio 03
'''
Scrivi una funzione che calcola la media di una lista di numeri 
e ritorna il valore arrotondato all'intero più vicino.
'''

def media_lista(lista_numeri:list[int]) -> int:
    somma = sum(lista_numeri)
    media = somma / len(lista_numeri)
    
    return round(media)

print(media_lista([5, 7, 9, 8]))



# Alternativo 
'''
Se la lista fosse composta da diversi tipi di elementi, come stringa, float, intero, booleano. 
Come potrei fare?
'''

def media_lista(lista_elementi:list) -> list[int, float, str, bool]:
    # per filtrare solo i numeri interi e float bisogna fare:
    numeri = [elemento for elemento in lista_elementi if isinstance(elemento, (int, float))]
    somma_numeri = sum(numeri)
    media_solo_numeri = somma_numeri / len(numeri)

    return round(media_solo_numeri, 2)


print(f"La media è: {media_lista([1, 'a', 59.65, True, 2, 36, 'aka', False])}")


def media_lista(lista_elementi:list) -> list[int, float, str, bool]:
    # per filtrare solo i numeri interi e float bisogna fare:
    numeri = [elemento for elemento in lista_elementi if isinstance(elemento, (int, float))]
    somma_numeri = sum(numeri)
    media_solo_numeri = somma_numeri / len(numeri)

    return round(media_solo_numeri)


print(f"La media dei numeri è: {media_lista([1, 'a', 59.65, True, 2, 36, 'aka', False])}")