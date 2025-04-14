# Esercizio 01
'''
Scrivi una funzione che calcoli i fattori primi di un numero intero positivo n.
Un fattore primo di n è un numero primo che divide esattamente n (cioè senza resto), 
e la cui moltiplicazione in sequenza restituisce n. Un numero può avere lo stesso fattore primo più volte.
'''

def prime_factors(n:int): 
 
    lista_fattori = []

    while n % 2 == 0:
        lista_fattori.append(2)
        n = n // 2
    
    elemento = 3
    while elemento * elemento <= n:
        while n % elemento == 0:
            lista_fattori.append(elemento)
            n = n // elemento
        
        elemento += 2 
    
    if n > 2:
        lista_fattori.append(n)
    
    return lista_fattori

print(prime_factors(4))
print(prime_factors(60))
