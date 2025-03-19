# Esercizio 02 - Trova il massimo tra 4 numeri

# Ciclo while
i = 1
num_max = float(input("Inserire un numero: "))

while i < 4:
    num = float(input("Inserire un numero: "))

    if num > num_max:
        num_max = num
    i += 1
print(f"Il numero massimo tra quelli inseriti è: {num_max}")


# Ciclo while (Repeat until)
i = 1
num_max = float(input("Inserire un numero: "))

while True:
    num = float(input("Inserire un numero: "))

    if num > num_max:
        num_max = num
    i += 1

    if i == 4:
        break
print(f"Il numero massimo tra quelli inseriti è: {num_max}")


# Ciclo for
num_max = float(input("Inserire un primo numero: "))

for i in range(3):
    num = float(input("Inserire un numero: "))
    if num > num_max:
        num_max = num
print(f"Il numero massimo tra quelli inseriti è: {num_max}")
