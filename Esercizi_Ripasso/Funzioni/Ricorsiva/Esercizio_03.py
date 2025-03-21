# Esercizio 3 - Somma tra a e b
''' "b" è maggiore di "a", altrimenti invertire il 
valore di "a" cosicchè "b" sia sempre maggiore di "a" '''

def somma_rango(a:int, b:int) -> None:
    if a > b:
        a, b = b, a
    
    if b == a:
        return int(a)

    else:
        return int(b + somma_rango(a, b - 1))

print(f"La somma tra 5 e 10 è: {somma_rango(5, 10)}")