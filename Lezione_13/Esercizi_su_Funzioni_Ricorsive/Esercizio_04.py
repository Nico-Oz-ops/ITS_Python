# Esercizio 4
'''
Scrivere una funzione ricorsiva recursiveDigitCounter che restituisca 
il numero di cifre di un numero intero n passato in input.
Sono permessi sia valori positivi che negativi per n.
Ad esempio, il numero -120 ha 3 cifre.
Non si tenga conto di eventuali zeri non significativi.
'''

def recursiveDigitCounter(n:int) -> int:

    if -9 <= n <= 9:
        return 1 #(return f"Il numero {n} ha 1 cifra")

    else:
        return int(1 + recursiveDigitCounter(n // 10))

print(recursiveDigitCounter(-501565464))
print(recursiveDigitCounter(464))



# 12345 / 10 = 1234.5
# 1234 / 10 = 123.4
# 123 / 10 = 12.3
# 12 / 10 = 1.2
# 1 / 10 = 0.1