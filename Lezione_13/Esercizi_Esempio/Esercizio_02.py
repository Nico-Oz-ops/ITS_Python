# Esercizio 2

def somma(n:int):
    if n < 0:
        print("Errore")
        return None
    else:
        somma = 0
        i = 0
        while i <= n:
            somma += i
            i += 1
        return somma

print(somma(5))
print(somma(-5))

