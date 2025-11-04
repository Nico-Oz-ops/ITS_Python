'''
Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che 
classifica i numeri in liste separate per numeri pari e dispari.

For example:

Test	
print(classifica_numeri([1, 2, 3, 4, 5, 6])) 
{'pari': [2, 4, 6], 'dispari': [1, 3, 5]}

print(classifica_numeri([]))
{'pari': [], 'dispari': []}
'''
def classifica_numeri(lista: list[int]) -> dict[str:list[int]]:
    risultato = {"pari": [], "dispari": []}

    for numero in lista:
        if numero % 2 == 0:
            risultato["pari"].append(numero)
        else:
            risultato["dispari"].append(numero)
    
    return risultato

print(classifica_numeri([1, 2, 3, 4, 5, 6])) 

