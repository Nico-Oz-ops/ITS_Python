# Exercise 14 - Invertire un numero intero

# Opzione 1 - slicing
# n = int(input("Inserire un numero intero: ")[::-1])
# print(n)


# Opzione 2
n = int(input("Inserire un numero intero: "))
reverse = 0

while n > 0:

    cifra = n % 10 # se ottiene l'ultima cifra del numero
    reverse = reverse * 10 + cifra # costruisce il numero invertito
    n = n // 10 # rimuove l'ultima cifra
    
print(reverse)
