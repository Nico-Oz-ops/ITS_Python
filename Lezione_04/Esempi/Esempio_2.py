# 2 - Usando una funzione, sommare tra 1 e 10, 20 e 37 e 35 e 49.

def sum(a, b):
    
    somma = 0

    for i in range(a, b + 1):
        somma += i
    
    return somma

print(f"La somma tra 1 e 10 è {sum(1, 10)}")
print(f"La somma tra 20 e 37 è {sum(20, 37)}")
print(f"La somma tra 35 e 49 è {sum(35, 49)}")