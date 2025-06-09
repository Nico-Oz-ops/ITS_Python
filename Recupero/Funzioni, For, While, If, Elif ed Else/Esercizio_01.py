# Esercizio 01

'''
Funzioni, For, While, If, Elif ed Else
1) Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
oppure "Azione negata" a seconda delle condizioni che sono soddisfatte.
2) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
dato valore intero definito threshold.
3) Scrivere in Python dei cicli che stampino le seguenti sequenze di valori:
a) 2, 4, 6, 8, 10, 12, 14
b) 1, 4, 7, 10, 13
c) 30, 25, 20, 15, 10, 5, 0
d) 5, 15, 25, 35, 45
'''

# 1 
def combinazione_condizioni(x: bool, y: bool, z: bool) -> str:
    if x == True and (y or z) == True:
        return "Azione permessa"
    
    else:
        return "Azione negata"

print(combinazione_condizioni(True, False, True))
print("-" * 50)

# 2
def treshold_multiplicazione(lista: list[int], treshold: int) -> int:
    prodotto = 1

    for numero in lista:
        if numero < treshold:
            prodotto *= numero
    return prodotto

print(treshold_multiplicazione([2, 5, 88, 4, 7, 9], 50))
print("-" * 50)

# Opzionale A
def fattoriale(numero: int) -> int:
    fattoriale = 1

    for i in range(numero):

        fattoriale *= numero - i

    return fattoriale

print(fattoriale(5))
print("-" * 50)

# Opzionale B
def fattoriale(numero: int) -> int:
    fattoriale = 1

    for i in range(1, numero + 1):

        fattoriale *= i

    return fattoriale

print(fattoriale(5))
print("-" * 50)

# 3a
print("Esercizio 3A")
lista = []
for i in range(2, 14 + 1, 2):
     lista.append(i)
print(*lista)
print("-" * 50)

# 3b
print("Esercizio 3B")
lista = []
for i in range(1, 14, 3):
    lista.append(i)
print(*lista)
print("-" * 50)

# 3c
print("Esercizio 3C")
lista = []
for i in range(30, -5, -5):
    lista.append(i)
print(*lista)
print("-" * 50)

# 3d - 1
print("Esercizio 3D")
lista = []
for i in range(5, 45 + 1, 10):
    lista.append(i)
print(*lista)
print("-" * 50)

# 3d - 2
print("Esercizio 3D")
lista = [5, 15, 25, 35, 45]
print(", ".join(str(x) for x in lista))

# 3d - 3
#list comprehension
a = [i for i in range(5, 50, 10)]
print(*a)


