# Esercizio 02 - Identificare il tipo di dato
'''Verifica il tipo di una variabile utilizzando match. 
Prova a identificare se è un intero, una stringa, una lista o altro.'''

variabile = "ciao"

match variabile:
    case int():
        print(f"{variabile} è un intero")
    case str():
        print(f"{variabile} è una stringa.")
    case list():
        print(f"{variabile} è una lista")
    case _:
        print(f"{variabile} è un altro tipo di valore.")