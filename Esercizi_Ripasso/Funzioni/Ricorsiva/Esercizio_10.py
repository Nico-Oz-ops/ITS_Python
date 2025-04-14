# Esercizio 10
'''
Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo. 
Sia Pi una produttoria definita come segue:
Pi = (0 + 2) * (1 + 2) * (2 + 2) * ... * (n + 2).  

Calcolare il valore della produttoria Pi se n = 7.
'''

def recursiveProduttoria(n:int) -> int:
    if n == 0:
        return 2
    
    else:
        return int((n + 2) * recursiveProduttoria(n - 1))

print(f"Il valore della produttoria Pi se n = 7, è: {recursiveProduttoria(7)}")