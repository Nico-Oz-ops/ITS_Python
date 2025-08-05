'''
Tema: Liste e dizionari
Obiettivo: Identificare elementi ripetuti in una lista

Nome dell’esercizio: Trova elementi duplicati

Traccia:
Scrivi una funzione elementi_duplicati(lista) che prende una lista di elementi (numeri o stringhe) 
e restituisce un set contenente solo gli elementi che appaiono più di una volta.

elementi = ["a", "b", "c", "a", "d", "b", "e", "f", "f"]
elementi_duplicati(elementi)  # Output atteso: {'a', 'b', 'f'}

Suggerimento:
Usa un dizionario per contare quante volte ogni elemento compare. 
Poi filtra quelli con valore > 1. Puoi usare anche set o filter + lambda se vuoi sperimentare.
'''
# Opzione 1
def elementi_duplicati(elementi: list[int|float|str]) -> set[int|float|str]:

    conteggio = {}

    for elemento in elementi:
        if elemento not in conteggio:
            conteggio[elemento] = 1
        else:
            conteggio[elemento] += 1
    
    risultato = set()

    for elemento in conteggio:
        if conteggio[elemento] > 1:
            risultato.add(elemento)
    
    return risultato

elementi = ["a", "b", "c", "a", "d", "b", "e", "f", "f"]
print(elementi_duplicati(elementi))



# Opzione 2 - uso di filter e lambda
def elementi_duplicati(elementi: list[int|float|str]) -> set[int|float|str]:

    conteggio = {}

    for elemento in elementi:
        if elemento not in conteggio:
            conteggio[elemento] = 1
        else:
            conteggio[elemento] += 1
    
    return set(filter(lambda elemento: conteggio[elemento] > 1, elementi))

elementi = ["a", "b", "c", "a", "d", "b", "e", "f", "f"]
print(elementi_duplicati(elementi))


# Opzione 3 - set comprehension
def elementi_duplicati(elementi: list[int|float|str]) -> set[int|float|str]:
    conteggio = {}
    for elemento in elementi:
        conteggio[elemento] = conteggio.get(elemento, 0) + 1

    return {el for el in conteggio if conteggio[el] > 1}


# Opzione 4 - filter rimuovendo i doppioni dopo
def elementi_duplicati(elementi: list[int|float|str]) -> set[int|float|str]:
    conteggio = {}
    for elemento in elementi:
        conteggio[elemento] = conteggio.get(elemento, 0) + 1

    return set(filter(lambda el: conteggio[el] > 1, set(elementi)))