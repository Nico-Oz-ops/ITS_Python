'''
Tema: Stringhe e set - Caratteri unici
Obiettivo: Dato un elenco di stringhe, restituire tutti i caratteri che compaiono in tutte le stringhe.

Nome dell’esercizio: caratteri_comuni

Traccia:
Scrivi una funzione che prenda una lista di stringhe e restituisca un 
set contenente solo i caratteri presenti (caratteri in comune tra le stringhe) in ogni stringa della lista.

Input:
stringhe = ["casa", "sasso", "ascia"]

Suggerimento: puoi usare set e l’operatore di intersezione & oppure la funzione all().
'''
from functools import reduce

def caratteri_comuni(stringhe: list[str]) -> set[str]:
    # map(set, stringhe) trasforma ogni stringa in un set di caratteri. "casa" -> {'c', 'a', 's'}.

    # reduce(lambda a, b: a & b, ...) prende due set alla volta e calcola la loro intersezione (&).
    # Prima intersezione: set della prima e della seconda stringa
    # Poi intersezione con la terza stringa, e così via
    return reduce(lambda a, b: a & b, map(set, stringhe))

# reduce serve a “ridurre” una lista/iterabile a un unico 
# valore applicando una funzione binaria (che prende due argomenti) ripetutamente.

stringhe = ["casa", "sasso", "ascia"]
print(caratteri_comuni(stringhe))


def caratteri_comuni(stringhe: list[str]) -> set[str]:
    # Inizializzo il set comuni con i caratteri della prima stringa. "casa" ->{'c', 'a', 's'}.
    comuni = set(stringhe[0])
    # Si scorre le altre stringhe a partire dalla seconda ([1:]).
    for stringa in stringhe[1:]:
        # Converto la stringa corrente in un set di caratteri. -> set(stringa)
        # Calcolo l’intersezione con comuni. -> comuni.intersection()
        
        # Aggiorniamo comuni così da mantenere solo i caratteri presenti in tutte le stringhe viste finora.
        comuni = comuni.intersection(set(stringa))
    
    return comuni

stringhe = ["casa", "sasso", "ascia"]
print(caratteri_comuni(stringhe))