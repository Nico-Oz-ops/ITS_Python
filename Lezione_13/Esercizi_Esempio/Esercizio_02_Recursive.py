# Esercizio 2 - Recursive

def somma_ricorsiva(n:int):
    if n < 0:       # controllo se n è minore di 0
        print("Errore")
        return None
    
    elif n == 0:    # caso base
        return 0
    
    else:           # chiamata ricorsiva
        return int(n +  somma_ricorsiva(n - 1))
        
print(somma_ricorsiva(5))
print(somma_ricorsiva(-5))

