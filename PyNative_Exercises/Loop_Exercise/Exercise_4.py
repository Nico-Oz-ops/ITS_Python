# Exercise 4: Print multiplication table of a given number

# Opzione 1
num = int(input("Inserire un numero moltiplicatore: "))
limite = int(input("Inserire un numero limite: "))
prodotto = 1

for prodotto in range(1, limite + 1, 1):
    prodotto *= num
    print(prodotto)

# Opzione 2
num = int(input("Inserire un numero moltiplicatore: "))
prodotto = 1

for prodotto in range(1, 10 + 1, 1):
    prodotto *= num
    print(prodotto)




