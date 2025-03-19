# Esercizio 8 - Determinare la somma dei numeri dentro un intervallo

while True:
    num_A = input("Inserire un valore intero positivo A: ")

    if num_A.isdigit() and int(num_A) > 0:
        num_A = int(num_A)
        break

    else:
        print("Errore: il valore di \"A\" deve essere intero e positivo. Riprova a inserire un valore")

while True:
    num_B = input("Inserire un valore intero positivo B: ")

    if num_B.isdigit() and int(num_B) > 0:
        num_B = int(num_B)
        break

    else:
        print("Errore: il valore di \"A\" deve essere intero e positivo. Riprova a inserire un valore")

if num_A >= num_B:
    print("Errore: A deve essere minore di B")
else:
    somma = sum(range(num_A, num_B + 1))
    print(f"La somma dei numeri tra {num_A} e {num_B} è: {somma}")





