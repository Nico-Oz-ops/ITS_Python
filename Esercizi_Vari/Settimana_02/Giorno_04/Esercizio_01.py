'''
Tema: Ricorsione con condizioni più complesse
Obiettivo: Calcolare la somma di tutte le cifre pari di un numero intero positivo, usando la ricorsione.
'''

# Esercizio 01
# Titolo: "Somma cifre pari"

'''
Traccia
Scrivi una funzione ricorsiva somma_cifre_pari(n: int) -> int che prende un 
intero positivo n e restituisce la somma di tutte le sue cifre pari (0, 2, 4, 6, 8).

Suggerimento
Puoi usare:
* n % 10 → ultima cifra
* n // 10 → rimuove l’ultima cifra
* Se la cifra è pari (% 2 == 0), aggiungila alla somma ricorsiva
'''

def somma_cifre_pari(n: int) -> int:
    if n <= 0:
        return 0
    
    ultima_cifra = n % 10
    resto = n // 10

    if ultima_cifra % 2 == 0:
        return ultima_cifra + somma_cifre_pari(resto)
    
    else:
        return somma_cifre_pari(resto)

print(somma_cifre_pari(12547963))