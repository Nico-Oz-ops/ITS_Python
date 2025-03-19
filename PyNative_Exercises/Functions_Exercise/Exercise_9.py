# Exercise 9 - Trova l'elemento più grande da un elenco dato

# Opzione 1 - funzione integrata (max())
# x = [4, 6, 8, 24, 12, 2]
# valore_maggiore = max(x)
    
# print(valore_maggiore)

# Opzione 2
# def elemento_maggiore():
#     x = [4, 6, 8, 24, 12, 2]
#     num_max = x[0] # si inizia con il primo elemento della lista come il massimo

#     for i in x: # si itera su ogni elemento della lista x
#         if i > num_max: # se trovo un numaggiore di num_max
#             num_max = i # allora si aggiorna num_max
#     return num_max # restituisce il numero massimo trovato

# print(elemento_maggiore())


def elemento_maggiore():
    x = []
    n = int(input("Quanti numeri interi vuoi inserire?: "))
    i = 0
    while i < n:
        num = int(input(f"Inserire un {i + 1}° valore intero alla lista: "))
        x.append(num)
        i += 1

    num_max = x[0]
    for item in x:
        if item > num_max: 
            num_max = item
    return num_max 

print(f"L'elemento maggiore della lista è: {elemento_maggiore()}")

