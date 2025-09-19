'''
Esercizio 8 - Ordinamento personalizzato

Tema: Ordinamento liste
Obiettivo: Ordinare in base a criterio

Traccia:
Scrivi una funzione che, data una lista di stringhe, 
ritorni una nuova lista ordinata in base alla lunghezza delle stringhe.
'''
# Alternativa 1
def lista_ordinata(stringhe: list[str]):
    n = len(stringhe)

    for i in range(n):
        for j in range(0, n - i - 1):
            if len(stringhe[j]) > len(stringhe[j + 1]):
                stringhe[j], stringhe[j + 1] = stringhe[j + 1], stringhe[j]
    
    return stringhe

stringhe = ["lisa", "caccami", "adesso"]
print(lista_ordinata(stringhe))


def lista_ordinata(stringhe: list[str]):
    n = len(stringhe)

    for i in range(n):
        for j in range(0, n - i - 1):
            if len(stringhe[j]) < len(stringhe[j + 1]):
                stringhe[j], stringhe[j + 1] = stringhe[j + 1], stringhe[j]
    
    return stringhe

stringhe = ["lisa", "caccami", "adesso"]
print(lista_ordinata(stringhe))

# Alternativa 2 
def lista_ordinata(stringhe: list[str]):
    vocali = ["a", "e", "i", "o", "u"]
    return sorted(stringhe, key=lambda somma_vocali: sum(1 for count in somma_vocali if count in vocali))

stringhe = ["lisa", "caccami", "adesso"]
print(lista_ordinata(stringhe))

def lista_ordinata(stringhe: list[str]):
    return sorted(stringhe, key=len)

stringhe = ["lisa", "caccami", "adesso"]
print(lista_ordinata(stringhe))

# Alternativa 3
def lista_ordinata(stringhe: list[str]):
    stringhe.sort(key=len)
    return stringhe

stringhe = ["lisa", "caccami", "adesso"]
print(lista_ordinata(stringhe))
