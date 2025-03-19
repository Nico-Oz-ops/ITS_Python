# Exercise 13 - Trova il fattoriale di un numero dato

n = int(input("Inserire un numero intero: "))
fattoriale = 1

if n < 0:
    print("Non esiste un numero fattoriale negativo.")
elif n == 0:
    print("Il fattoriale di 0 è 1.")
else:
    for i in range(1, n + 1):
        fattoriale *= i
    print(f"Il numero fattoriale di {n} è \"{fattoriale}\".")