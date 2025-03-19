# Exercise 6: Contare il numero totale di cifre in un numero

n = int(input("Inserire un numero: "))
contatore = 0

while n != 0:
    n = n // 10
    contatore += 1

print(contatore)