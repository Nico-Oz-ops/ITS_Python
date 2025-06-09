# Esercizio 2
'''
Ricerca Binaria
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interi ordinati
e ritorna True se il numero è all’interno della lista, altrimenti False.
'''

def ricerca_binaria(lista: list[int], numero_da_cercare: int) -> bool:
    lista_ordinata = sorted(lista)

    inizio = 0
    finale = len(lista_ordinata) - 1

    while inizio <= finale:

        mezzo = (inizio + finale) // 2

        if lista_ordinata[mezzo] == numero_da_cercare:
            return True
        
        elif lista_ordinata[mezzo] < numero_da_cercare:
            inizio = mezzo + 1
        
        else:
            finale = mezzo - 1
        
    return False

list_1 = [1, 5, 9, 7, 6, 8, 3, 10] 
print(ricerca_binaria(list_1, 7))
print(ricerca_binaria(list_1, 11))
   




