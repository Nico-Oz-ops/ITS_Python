'''
Pronuncia `powerset_size(n)`: restituisci il numero di sottoinsiemi di un insieme con `n` elementi. 
'''

def powerset_size(n: int) -> int:
    if n < 0:
        raise ValueError("Errore, n deve essere positivo")
    return 2 ** n

print(powerset_size(3))

