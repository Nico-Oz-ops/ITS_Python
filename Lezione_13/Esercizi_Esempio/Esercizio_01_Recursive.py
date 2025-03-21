# Recursive countdown

def countdown(n:int) -> None:
    # n minore di 0
    if n < 0:              # Caso di base
        print("Errore!") 
    # n uguale di 0
    elif n == 0:
        print(0)
    # n si trova tra 1 e 5
    else:                   # Caso ricorsivo
        print(n)
        countdown(n - 1)

countdown(5)
