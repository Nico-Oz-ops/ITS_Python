'''
Tema: Ricorsione su numeri
Obiettivo: Contare quante cifre pari contiene un numero intero positivo, usando la ricorsione.
'''

# Esercizio 03
# Titolo: "Conta cifre pari"

'''
Traccia:
Scrivi una funzione ricorsiva che prende un numero intero positivo n e restituisce il numero di cifre pari contenute al suo interno.

Una cifra è pari se è 0, 2, 4, 6, 8.

Suggerimento (se ti serve):
Puoi usare:

* n % 10 → per ottenere l’ultima cifra
* n // 10 → per accorciare il numero

Controlla se l’ultima cifra è pari, poi chiama ricorsivamente la funzione sul resto del numero.
'''

def conta_cifre_pari(n: int) -> int:
    if n == 0:
        return 0
    
    ultima_cifra = n % 10
    resto = n // 10

    if ultima_cifra % 2 == 0:
        return 1 + conta_cifre_pari(resto)
    
    else:
        return conta_cifre_pari(resto)

print(conta_cifre_pari(1234567890))
print(conta_cifre_pari(135))



