# Esercizio 05 - Verifica se un numero è primo

import math

n = int(input("\nInserire un numero intero positivo: "))
limite = int(math.sqrt(n))
num_primo = True

# Opzione 1 - Uso ciclo for con iterazioni fino a radice quadrata di "n"
if n < 0:
    print(f"{n} non è un numero intero positivo")
else:
    if n < 2:
        num_primo = False
    else:
        for k in range(2, (limite) + 1):
            if n % k == 0:
                num_primo = False
                break

    if num_primo == True:
        print(f"{n} è primo")
    else:
        print(f"{n} non è primo")


# Opzione 2 - Uso ciclo for, con iterazioni fino ad "n"

if n < 0:
    print(f"{n} non è un numero positivo")
else:
    if n < 2:
        num_primo = False
    else:
        for i in range(2, n):
            if n % i == 0:
                num_primo = False
                break
    
    if num_primo:
        print(f"{n} è primo")
    else:
        print(f"{n} non è primo")

# Opzione 3 -Uso di ciclo while, con iterazioni fino alla radice quadrata di "n"

if n < 0:
    print(f"{n} non è un numero positivo")
else:
    if n < 2:
        num_primo = False
    else:
        divisore = 2
        while divisore <= limite:
            if n % divisore == 0:
                num_primo = False
                break
            divisore += 1
    
    if num_primo:
        print(f"{n} è primo")
    else:
        print(f"{n} non è primo")        



