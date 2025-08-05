'''
Tema:  Ricorsione + decomposizione numerica
Obiettivo: Scrivere una funzione ricorsiva che calcoli il prodotto di tutte le cifre dispari di un numero intero positivo.
'''

# Esercizio 01
# Titolo: "Prodotto_cifre_dispari"

'''
Traccia:
Definisci la funzione prodotto_cifre_dispari(n: int) -> int che prende in input un 
numero positivo n e restituisce il prodotto di tutte le cifre dispari contenute nel numero.
Se non ci sono cifre dispari, restituisci 1.

Non usare cicli (for, while), solo ricorsione.

Suggerimento
* Per ottenere l’ultima cifra: n % 10
* Per “accorciare” il numero: n // 10
* Usa il caso base n == 0 per fermare la ricorsione
'''

def prodotto_cifre_dispari(n: int) -> int:
    if n == 0:
        return 1
    
    ultima_cifra = n % 10
    resto = n // 10

    if ultima_cifra % 2 == 1:
        return ultima_cifra * prodotto_cifre_dispari(resto)
    else: 
        return prodotto_cifre_dispari(resto)

print(prodotto_cifre_dispari(37258))
    


    