# Esercizio 6 - Somma condizionata di numeri in base a un valore x

x = float(input("Inserire un valore positivo: "))

if x > 0:

    i = 0
    somma = 0

    for i in range(5):
        n = float(input(f"Inserire un {i + 1}° valore positivo e/o negativo: "))

        if x % 2 == 0:
            if n > x / 2:
                somma += n

        else: 
            if n < x:
                somma += n  

        i += 1

    print(f"La somma dei numeri quando x: {x} è uguale a: {somma}")
    
else:
    print("Errore, il valore inserito deve essere positivo. Addio")
