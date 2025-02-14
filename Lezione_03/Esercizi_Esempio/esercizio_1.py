# Inserire 6 numeri interi scelti dall'utente. 
# Di questi 6 numeri, sommare solo i numeri pari.

# Modo I - Ciclo while
print("Modo I - While:")
i:int = 1 
somma:int = 0

while i <= 6:
    # inserire un numero
    n:int = int(input("Digita un numero intero: "))
    
    if n % 2 == 0:
        somma += n
    i += 1 
# print(f"somma: {somma}")

# Modo II - Ciclo For
print("Modo II - For:")
somma:int = 0

for i in range(6):
    n:int = int(input("Digitare un numero intero: "))
    if n % 2 == 0:
        somma += n 
print(f"Somma: {somma}")
    