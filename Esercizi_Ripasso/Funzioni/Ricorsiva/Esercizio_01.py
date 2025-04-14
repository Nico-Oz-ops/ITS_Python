# Esercizio 01 - Funzione Ricorsiva
'''Calcolare il fattoriale'''

# Opzione ciclo while
while True:
    n = input("Inserire un numero intero positivo: ")
    if n.isdigit() and int(n) >= 0:
        n = int(n)
        break
    else:
        print("Errore. Inserire un numero intero e positivo")

if n == 0:
    print("Il fattoriale di 0 è 1")

else:
    i = 1
    fattoriale = 1
    while i <= n:
        fattoriale *= i
        i += 1
    print(f"Il fattoriale di {n} è: {fattoriale}")


# Opzione funzione ricorsiva

def fattoriale(num:int):
    if num < 0:
        print("Errore")
    
    elif num == 0:
        return 1
    
    else:
        return num * fattoriale(num - 1)

print(f"Il fattoriale di 5 è: {fattoriale(5)}")
    
