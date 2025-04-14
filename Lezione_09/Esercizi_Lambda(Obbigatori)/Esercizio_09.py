# Esercizio 09
'''
Ritorna una lambda
Scrivi una funzione moltiplicatore(n) 
che ritorni una lambda che moltiplica un valore per n.
'''

def moltiplicatore(n):
    return lambda num: num * n

per_due = moltiplicatore(2)
print(per_due(10))

print("-" * 50)

def molt(m:int, n:int) -> int:
    return m * n

moltiplicatore = molt(2, 5)
print(moltiplicatore)
