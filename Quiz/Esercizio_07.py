# Esercizio 7
'''
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
'''
def check_parentheses(expression:str) -> bool:
    count = 0

    for carattere in expression:
        if carattere == "(":  # incremento quando si trova una parentesi aperta
            count += 1

        elif carattere == ")": # decremento se trova una parentesi chiusa
            count -= 1
        
        if count < 0: # Se il contatore diventa negativo, significa che c'è una parentesi chiusa senza una corrispondente aperta
            return False

    return count == 0 # se alla fine il contatore "count" è uguale a zero, vuol dire che sono bilanciate


print(check_parentheses("()()"))
print(check_parentheses("(()))("))




















# count = 0
# bilanciate = True
# stringa = input("Inserire una stringa di parentesi:")

# for carattere in stringa:
#     if carattere == "(":
#         count += 1
#     elif carattere == ")":
#         count -= 1
#     if count < 0:
#         bilanciate = False
#         break

# if count != 0:
#     bilanciate = False

# print(bilanciate)