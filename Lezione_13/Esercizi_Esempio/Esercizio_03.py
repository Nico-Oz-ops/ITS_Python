# Esercizio 3

# Opzione 1
def suminRange(a:int, b:int) -> None:
    
    if a > b:
        a, b = b, a
    
    somma = 0

    while a <= b:
        somma += a
        a += 1
    
    return somma

print(suminRange(15, 10))

print(suminRange(10, 15))


# Opzione 2
def suminRange(a:int, b:int) -> None:
    
    if a > b:
        
        temp:int = a # variabile temporanea che ospita il valore (temporaneamente) di "a"

        a = b
        b = temp
    
    somma = 0

    while b >= a:
        somma += b
        b -= 1
    
    return somma

print(suminRange(5, 10))

print(suminRange(10, 5))