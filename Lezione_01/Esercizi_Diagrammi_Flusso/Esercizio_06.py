# Esercizio 06 - Calcolo del fattoriale di un numero

# Ciclo for

n = int(input("Inserire un numero intero positivo: "))
fattoriale = 1
# i = 1

if n < 0:
    print(f"{n} deve essere un numero intero e positivo")
elif n == 0:
    print(f"Il fattoriale di {n} è: 1")
else:
    for i in range(1, n + 1):
        fattoriale *= i
    print(f"Il fattoriale di {n} è: {fattoriale}")

print("-" * 30)

# # Ciclo While
# n_1 = int(input("Inserire un numero intero positivo: "))
# fattoriale_1 = 1
# i_1 = 1

# if n_1 < 0:
#     print(f"{n_1} deve essere un numero intero e positivo")
# elif n_1 == 0:
#     print(f"Il fattoriale di {n_1} è: 1")
# else:
#     while i_1 <= n_1:
#         fattoriale_1 *= i_1
#         i_1 += 1
#     print(f"Il fattoriale di {n_1} è: {fattoriale_1}")


