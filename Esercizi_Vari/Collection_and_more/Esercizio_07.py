'''
Tema: Liste, all(), lambda, map - Verifica globale su più condizioni

Obiettivo: Usare all() e lambda per verificare se tutti gli elementi di una lista soddisfano una combinazione di condizioni.

Nome dell’esercizio: Tutti validi?

Traccia:
Scrivi una funzione tutti_valori_validi(numeri: list[int]) -> bool che restituisce True se tutti i numeri nella lista sono:

* pari
* positivi

Altrimenti restituisce False.

Esempio:
tutti_valori_validi([2, 4, 8, 12])       ➝ True  
tutti_valori_validi([2, -4, 8])          ➝ False  
tutti_valori_validi([2, 3, 4])           ➝ False  

Suggerimento
Puoi usare all() combinato con map() oppure con una list comprehension o generator expression.
'''

def tutti_valori_validi(numeri: list[int]) -> bool:
    # Verifico se ogni numero della lista è positivo e pari. Se anche uno non lo è, restituisci False.
    # map() ha bisogno di 2 parametri, una funzione come lambda o anche del tipo def, e un iterabile come dict, list, set...
    return all(map(lambda numero: numero % 2 == 0 and numero > 0, numeri))

numeri_1 = ([2, 4, 8, 12])      
numeri_2 = ([2, -4, 8])          
numeri_3 = ([2, 3, 4]) 

print(tutti_valori_validi(numeri_1))
print(tutti_valori_validi(numeri_2))
print(tutti_valori_validi(numeri_3))

# Alternativa senza uso di map() e lambda - generator expression
def tutti_valori_validi(numeri: list[int]) -> bool:
    return all(numero % 2 == 0 and numero > 0 for numero in numeri)

numeri_a = ([2, 4, 8, 12])      
numeri_b = ([2, -4, 8])          
numeri_c = ([2, 3, 4]) 

print(tutti_valori_validi(numeri_a))
print(tutti_valori_validi(numeri_b))
print(tutti_valori_validi(numeri_c))