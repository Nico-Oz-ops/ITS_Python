'''
Tema: Ricorsione semplice
Obiettivo: Scrivere una funzione ricorsiva che calcoli la somma delle cifre di un numero intero positivo.
'''

# Esercizio 05
# Titolo: "Somma delle cifre"

'''
Traccia:
Scrivi una funzione che prende un numero intero positivo n e restituisce la somma delle sue cifre.
Ad esempio:

somma_cifre(1234) → 1 + 2 + 3 + 4 = 10

Vincoli:

* Usa solo la ricorsione
* Niente str(), cicli, né funzioni come sum() o map().

Suggerimento:
Puoi ottenere l’ultima cifra con n % 10 e il numero senza l’ultima cifra con n // 10.
'''

def somma_cifre(n: int) -> int:
    print(f"Chiamata con n = {n}") # proposta di Chat per vedere come lavora la funzione passo a passo
    if n < 10:
        return n
    else:
        return (n % 10) + somma_cifre(n // 10)
    
print(somma_cifre(1234))


