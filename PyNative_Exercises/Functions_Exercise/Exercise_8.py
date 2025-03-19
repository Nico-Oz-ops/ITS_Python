# Exercise 8 - Genera un elenco Python di tutti i numeri pari compresi tra 4 e 30

def num_pari():
    pari = []
    for i in range(4, 30, 2):
        pari.append(i)
    print(pari)

num_pari()


# Opzione scala piramidale
def num_pari():
    pari = []
    for i in range(4, 30 + 1, 2):
        pari.append(i)
        print(pari)

num_pari()