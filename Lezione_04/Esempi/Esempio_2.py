# 2 - Usando una funzione, sommare tra 1 e 10, 20 e 37 e 35 e 49.

# Opzione 1
def sum(a, b):
    somma = 0 # define a sum to be computed

    for i in range(a, b + 1): # compute a sum
        somma += i

    return somma # return the value of sum as the output of the sum function

# print(f"La somma tra 1 e 10 è {sum(1, 10)}")
# print(f"La somma tra 20 e 37 è {sum(20, 37)}")
# print(f"La somma tra 35 e 49 è {sum(35, 49)}")


# Opzione 2

def sum(a, b):
    somma = 0

    for i in range(a, b + 1):
        somma += i

    return somma

mysum = sum(1, 10)
# print(f"La somma da 1 a 10 è: {mysum}")
print(type(sum(1, 10)))
    