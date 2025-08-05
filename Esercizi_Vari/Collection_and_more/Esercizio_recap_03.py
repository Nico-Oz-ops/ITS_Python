'''
Tema: all e condizioni
Obiettivo: Uso corretto di all con map

Nome dell’esercizio: Tutti multipli di 3?

Traccia:
Scrivi una funzione tutti_multipli_di_3(numeri: list[int]) -> bool che restituisce True 
se tutti i numeri nella lista sono multipli di 3, False altrimenti.

Suggerimento:
Puoi usare all(map(lambda x: ..., numeri)).
'''
# Alternativa 1 - all()-map()-lambda
def tutti_multipli_di_3(numeri: list[int]) -> bool:
    return all(map(lambda numero: numero % 3 == 0, numeri))

numeri = [1, 8, 6, 4, 9, 66, 30, 45, 15, 20, 21, 11]
numeri_2 = [3, 12, 21, 30]
print(tutti_multipli_di_3(numeri))
print(tutti_multipli_di_3(numeri_2))

# Alternativa 2 - (generator expression)
def tutti_multipli_di_3_b(numeri: list[int]) -> bool:
    return all(numero % 3 == 0 for numero in numeri )

numeri_a = [30, 45, 15, 20, 21, 11]
numeri_b = [3, 12, 21, 30]
print(tutti_multipli_di_3_b(numeri_a))
print(tutti_multipli_di_3_b(numeri_b))