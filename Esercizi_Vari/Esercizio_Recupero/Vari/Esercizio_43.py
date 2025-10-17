'''
Verifica

Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, Z) è soddisfatta per
procedere con un'azione. L'azione può procedere solo se la condizione X è vera e almeno una tra Y e Z
è vera. La funzione deve ritornare "Azione permessa" oppure "Azione negata" a seconda delle condizioni che sono 
soddisfatte
'''

def verifica(X: bool, Y: bool, Z: bool) -> str:
    if X and (Y or Z):
        return "Azione permessa"
    
    return "Azione negata"

print(verifica(True, True, True))
print(verifica(True, False, True))
print(verifica(True, True, False))
print(verifica(True, False, False))
print(verifica(False, True, True))
print(verifica(False, False, True))
print(verifica(False, False, False))