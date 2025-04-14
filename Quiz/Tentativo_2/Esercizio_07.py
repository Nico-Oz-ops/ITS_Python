# Esercizio 07
'''Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.'''

def check_parentesi(espressione:str) -> bool:
    
    count = 0

    for carattere in espressione:

        if carattere == "(":
            count += 1

        elif carattere == ")":
            count -= 1

        if count < 0:
            return False
    
    if count == 0:
        return True

print(check_parentesi("()()"))
print(check_parentesi("(()))("))


