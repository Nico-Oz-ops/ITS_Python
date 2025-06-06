# Esercizio 3
'''
Fattoriale
Calcola il fattoriale di un numero n (es: 5! = 5x4x3x2x1).
'''

def fattoriale(numero: int) -> int:

    risultato = 1

    for i in range(1, numero + 1):
        risultato *= i
    
    return f"Il fattoriale di {numero} è: {risultato}"

print(fattoriale(5))


