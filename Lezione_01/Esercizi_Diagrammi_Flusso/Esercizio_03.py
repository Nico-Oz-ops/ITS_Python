# Esercizio 03 - Calcolare la somma di numeri positivi

sum = 0
cont = 0

while True:
    n = float(input("Inserire un numero intero positivo: "))
    if n > 0:
        sum += n
    cont += 1

    if cont == 5:
        break
print(f"La somma {sum}")

