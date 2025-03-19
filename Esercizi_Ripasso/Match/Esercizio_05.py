# Esercizio 05 - Gestire una tupla
'''Verifica se una tupla ha due o più elementi 
e fai qualcosa in base al numero di elementi'''

tupla = (2,)

match tupla:
    case ():
        print("Non ci sono elementi nella tupla")
    case (a, b):
        print(f"La tupla ha 2 elementi: {a} e {b}")
    case (a,):
        print(f"La tupla ha 1 elemento: {a}")
    case _:
        print("La tupla ha più di 2 elementi")
