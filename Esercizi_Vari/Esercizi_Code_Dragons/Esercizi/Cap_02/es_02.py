'''
Compila `merge_overwrite(a, b)` per restituire un nuovo dizionario 
dove i valori di `a` sono sovrascritti dagli aggiornamenti in `b`.
'''
# Alternativa 1
def merge_overwrite(a: dict, b: dict) -> dict:
    risultato = a.copy()  # creo una copia di "a" per evitare di modificarla direttamente
    risultato.update(b)   # sovrascrivo i valori con quelli di "b"
    return risultato

# Alternativa 2
def merge_overwrite(a: dict, b: dict) -> dict:
    c = {}

    for chiave in a:
        c[chiave] = a[chiave]
    
    for chiave in b:
        c[chiave] = b[chiave]
    
    return c
