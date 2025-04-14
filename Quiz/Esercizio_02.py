# Esercizio 2 - countdown

def countdown(n:int) -> int:
    if n < 0:
        print("Errore")
    elif n == 0:
        print(0)
    else:
        print(n)
        countdown(n - 1)

countdown(5)

