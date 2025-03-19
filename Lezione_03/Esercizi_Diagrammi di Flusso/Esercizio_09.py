# Esercizio 9 - Conteggio dei numeri divisibili

while True:
    n = input("Inserire un valore intero positivo: ")

    if n.lstrip('-').isdigit():
        n = int(n)
        if n > 0:
            break
        else:
            print("Errore, il valore non è positivo. Addio")
            exit()

    else:
        print("Errore. Devi inserire un numero intero positivo")

cont = 0
i = 0
for i in range(10):
    while True:
        x = input(f"Inserire un {i + 1}° valore intero: ")

        if x.lstrip('-').isdigit():
            x = int(x)
            break
        else:
            print("Errore. Devi inserire un numero intero")

    if x % n == 0:
        cont += 1
    i += 1
    
print(f"I valori divisibili per {n} sono {cont}")




