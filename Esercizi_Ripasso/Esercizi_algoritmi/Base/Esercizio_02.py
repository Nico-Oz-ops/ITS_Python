# Esercizio 2
'''
Trova il massimo
Data una lista di numeri, restituisci il numero più grande.
'''

def massimo(numeri: list[float]) -> float:
   
    max = numeri[0]
    
    for numero in numeri:
        if numero > max:
            max = numero
    
    return f"Il numero massimo della lista è: {max}"

print(massimo([1, 25, 32.35, 78, 96.45]))
        
