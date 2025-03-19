# Esercizio 12 - Scelta condizionale basata su input multipli

while True:
    n = input("Inserire un numero: ")

    if n.lstrip("-").isdigit():
        n = int(n)
        break
    else:
        print("Errore. Riprova a inserire un numero")

i = 0

while i != n:
    while True:
        x = input(f"\nInserire un valore di X: ")

        if x.lstrip("-").isdigit():
            x = int(x)
            break
        else:
            print("Errore. Riprova a inserire un numero")
            
    while True:
        y = input("\nInserire un valore di Y: ")

        if y.lstrip("-").isdigit():
            y = int(y)
            break
        else:
            print("Errore. Riprova a inserire un numero")
    
    if x > 0 and y > 0:
        prodotto = x * y
        print(f"\nIl prodotto di X e Y è: {prodotto}")
    else:
        if x < 0 and y < 0:
            print("Errore")
        else:
            somma= x + y
            print(f"\nLa somma di X e Y è: {somma}")
    i += 1
    
    