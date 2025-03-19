# Esercizio 06 - Riconoscere il primo valore di una lista
'''Controlla se una lista ha un determinato primo elemento'''

lista = [3, 2.3, 8, 9]

match lista:
    case [1, *resto]:
        print(f"Il primo elemento della lista è 1 e il resto è: {resto}")
    case [2, *resto]:
        print(f"Il primo elemento della lista è 2 e il resto è: {resto}")
    case [3, *resto]:
        print(f"Il primo elemento della lista è 3 e il resto è: {resto}")
    case _:
        print("La lista inizia con un altro valore")