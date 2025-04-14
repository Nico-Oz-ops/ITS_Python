# Esercizio 2
'''
Convalida password:  scrivi una funzione validate_password(password) che controlli se una password 
soddisfa i seguenti criteri: lunghezza minima di 20 caratteri, almeno tre lettere maiuscole, almeno 
quattro caratteri speciali (non alfanumerici). Se la password è valida, la funzione dovrebbe restituire True. 
Se la password non è valida, la funzione dovrebbe sollevare un'eccezione incorporata (ad esempio, ValueError) 
con un messaggio che indica quali criteri non sono stati soddisfatti.
'''
import string

def validate_password(password):
    if len(password) < 20:
        raise ValueError("La password deve avere una lunghezza minima di 20 caratteri")
    
    upper_case_conta = sum(1 for cont in password if cont.isupper())
    if upper_case_conta < 3:
        raise ValueError("La password deve avere almeno 3 lettere maisucole")
    
    caratteri_speciali = string.punctuation
    caratteri_speciali_cont = sum(1 for cont in password if caratteri_speciali)
    if caratteri_speciali_cont < 4:
        raise ValueError("La password deve avere almeno 4 caratteri speciali")
    
    return True

try:
    print(validate_password("1258762jhkjsdAFDRGS45"))
except ValueError as e:
    print(e)

try:
    print(validate_password("12548j"))
except ValueError as e:
    print(e)