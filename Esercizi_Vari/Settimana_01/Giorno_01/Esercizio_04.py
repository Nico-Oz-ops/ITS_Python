'''
Obiettivo: Allenarti con il ciclo for e il concetto di somma incrementale.
'''

# Esercizio 04
# Titolo: Somma dei primi N numeri"

'''
Traccia:
Scrivi una funzione somma_primi_n(n: int) -> int che:

Prende un numero intero n come argomento.

Calcola la somma dei primi n numeri interi positivi, cioè da 1 a n inclusi.

Restituisce il risultato.

(Se vuoi puoi fare anche una versione con input() ma ti consiglio 
di farla prima con parametro, per abituarti alla scrittura di 
funzioni riutilizzabili)
'''

def somma_primi_n(n: int) -> int:

    somma = 0

    for num in range(1, n + 1):
        somma += num
    
    return somma

print(somma_primi_n(5))