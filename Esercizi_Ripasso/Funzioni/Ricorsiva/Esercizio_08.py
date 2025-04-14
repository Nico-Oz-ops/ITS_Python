# Esercizio 8
'''
Scrivere una funzione ricorsiva recursiveDigitCounter che 
restituisca il numero di cifre di un numero intero n passato in input.
Sono permessi sia valori positivi che negativi per n.
Ad esempio, il numero -120 ha 3 cifre.
Non si tenga conto di eventuali zeri non significativi.

Suggerimento: per il calcolo delle cifre, fare un controllo se il valore 
assoluto di n sia minore di 10. In caso positivo, significa che il 
numero n ha una sola cifra. In caso negativo, significa che il numero n ha più cifre; 
dunque, dividere n per 10 per rimuovere l'ultima cifra e richiama ricorsivamente la funzione, 
fino a ottenere un numero con una sola cifra.
'''

def recursiveDigitCounter(n:int) -> int:

    if -9 <= n <= 9:
        return 1
    
    else:
        return int(1 + recursiveDigitCounter(n // 10))

print(f"Il numero -8 ha: {recursiveDigitCounter(-8)} cifra.")
print(f"Il numero 19 ha: {recursiveDigitCounter(19)} cifre.")
print(f"Il numero 125 ha: {recursiveDigitCounter(125)} cifre.")
print(f"Il numero -1458 ha: {recursiveDigitCounter(-1458)} cifre.")