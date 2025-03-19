# Esercizio 07 - Conta i numeri pari e dispari

pari = 0
dispari = 0
cont = 0

# Ciclo While
while True:
    if cont == 10:
        break
    else:
        n = int(input("Inserire un numero: "))

        if n % 2 == 0:
            pari += 1
        else:
            dispari += 1
    cont += 1

print(f"Ci sono {pari} numeri pari")
print(f"Ci sono {dispari} numeri dispari")

# # Ciclo For
# for cont in range(10):
#     n = int(input("Inserire un numero intero: "))

#     if n % 2 == 0:
#         pari += 1
#     else:
#         dispari += 1
#     cont += 1
# print(f"Ci sono {pari} numeri pari")
# print(f"Ci sono {dispari} numeri dispari")