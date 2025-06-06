# Esercizio 5
'''
Somma cifre
Somma tutte le cifre di un numero intero (es: 123 → 1+2+3 = 6).
'''

def somma_cifre(numero) -> int:

    numero = abs(numero)

    return f"La somma di tutte le cifre di {numero} è: {sum(int(carattere) for carattere in str(numero))}"

print(somma_cifre(548))


def somma_cifra(num) -> int:
    num = abs(num)
    somma = 0

    for car in str(num):
        somma += int(car)
    
    return f"La somma di tutte le cifre di {num} e: {somma}"

print(somma_cifra(54))