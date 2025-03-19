# Esercizio 04 - Gestire numeri con diversi intervalli
'''Verifica se un numero rientra in un determinato intervallo di valori, 
come un numero negativo, compreso tra 0 e 10, o maggiore di 10.'''

numero = int(input("Inserire un numero intero: "))

match numero:
    case numero if numero < 0:
        print("Il numero inserito è negativo.")
    case numero if 0 <= numero <= 10:
        print(f"{numero} è compreso tra 0 e 10.")
    case _:
        print(f"{numero} è maggiore di 10.")