# Esercizio 03 - Verifica se una lista è vuota o contiene un solo elemento
'''Controlla se una lista è vuota o contiene esattamente un elemento, 
o se contiene più di un elemento.'''

lista = [2, 6, "asdf"]

match lista:
    case []:
        print("La lista è vuota")
    case [x]:
        print(f"La lista contiene un solo elemento: {x} ")
    case [x, y]:
        print(f"La lista contiene 2 elementi: {x} e {y}")
    case _:
        print("La lista contiene più di due elementi")