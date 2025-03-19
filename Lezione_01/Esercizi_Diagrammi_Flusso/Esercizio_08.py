# Esercizio 08 - Trovare i numeri maggiori di un valore soglia

soglia = float(input("Inserire un valore soglia: "))
cont = 0

# Ciclo wghile
while True:
    if cont == 7:
        break
    else:
        n = float(input("Inserire un numero: "))

        if n < soglia:
            print(f"{n} è minore della soglia, \"{soglia}\"")
        else:
            print(f"{n} è maggiore della soglia, \"{soglia}\"")
    cont += 1

# Ciclo for
for cont in range(7):
    n = float(input("Inserire un numero: "))
    if n < soglia:
        print(f"{n} è minore della soglia, \"{soglia}\"")
    else:
        print(f"{n} è maggiore della soglia, \"{soglia}\"")



