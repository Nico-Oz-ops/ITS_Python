# Exercise 1: Calculate the multiplication and sum of two numbers

# Opzione 1 - uso di if/else
# num_1 = int(input("Inserire un numero: "))
# num_2 = int(input("Inserire un numero: "))

# if (num_1 * num_2) <= 1000:
#     print(f"{num_1} x {num_2} = {num_1 * num_2}")
# else:
#     print(f"{num_1} + {num_2} = {num_1 + num_2}")

# Opzione 2 - uso di Funzione
def prodotto_o_somma(a, b) -> tuple[int, int]:
    mult = a * b
    somma = a + b
    if mult <= 1000:
        return mult
    else:
        return somma

risultato_1 = prodotto_o_somma(20, 30)
risultato_2 = prodotto_o_somma(40, 30)

print(f"Risultato 1: {risultato_1}")
print(f"Risultato 2: {risultato_2}")