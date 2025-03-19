# Exercise 6:

# def funzione_ricorsiva():
#     somma = 0
#     for i in range(10 + 1):
#         somma += i
#     return somma

# print(funzione_ricorsiva())


# Opzione 2 - funzione ricorsiva

def addition(num):
    if num:
        result = num + addition(num - 1)
        
        return result
    
    else:
        return 0

print(addition(10))