'''
Verifica l'incanto con `are_anagrams(a, b)`: ritorna `True` se le due parole/frasi usano 
le **stesse lettere** al netto degli **spazi** e delle **maiuscole**, altrimenti `False`
'''

def are_anagrams(a: str, b: str) -> bool:
    parola_a = a.replace(" ", "").lower()
    parola_b = b.replace(" ", "").lower()

    if sorted(parola_a) == sorted(parola_b):
        return True
    return False

a = "Adios"
b = "sadio"
print(are_anagrams(a, b))