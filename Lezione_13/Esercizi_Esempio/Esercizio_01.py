# Esercizio 1

# Ciclo while
def countdown (n:int) -> None:
    if n >= 0:
        while n >= 0:
            print(n)
            n -= 1
    else:
        print("Errore, il numero inserito è negativo")

countdown(-5)
print("-" * 50)
countdown(5)

# Ciclo for
def countdown(n):
    if n >= 0:
        for i in range(n, -1, -1):
            print(i)
    else:
        print("errore")

countdown(5)
countdown(-5)