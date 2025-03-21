# Esercizio 3 - funzione recursiva

def recursivesuminRange(a:int, b:int) -> None:
    if a > b:
        temp = a
        a = b
        b = temp
    
    if b == a:      # caso base
        return a
    
    else:           # chiamata ricorsiva       
        return int(b + recursivesuminRange(a, b - 1))

print(recursivesuminRange(5, 10))
print("-" * 50)
print(recursivesuminRange(10, 5))

