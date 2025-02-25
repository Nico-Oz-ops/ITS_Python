n1 = int(input("Inserire un numero intero: "))
n2 = int(input("Inserire un secondo numero intero: "))

prodotto = 1
if n1 > n2:
    for numero in range(n2, n1 + 1):
        prodotto *= numero
else:
    for numero in range(n1, n2 + 1):
        prodotto *= numero

print(f"Il prodotto di tutti i numeri interi compresi tra \"{n1}\" e \"{n2}\" è: \"{prodotto}\"")