'''
Esegui `invert_unique(d)`, che inverte chiavi e valori assumendo 
valori univoci.
'''

def invert_unique(d: dict) -> dict:
    return {chiave: valore for valore, chiave in d.items()}