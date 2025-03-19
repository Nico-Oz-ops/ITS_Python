# Exercise 4

def check_each(lista):
    for elemento in lista:
        if elemento > 5:
            print(f"{elemento} è maggiore di 5")
        elif elemento < 5:
            print(f"{elemento} è minore di 5")
        else: 
            print(f"{elemento} è uguale a 5")     

check_each([1, 5, 6])     

