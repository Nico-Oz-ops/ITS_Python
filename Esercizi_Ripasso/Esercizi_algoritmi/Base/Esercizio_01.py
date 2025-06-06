# Esercizio 1
'''
Pari o dispari
Scrivi una funzione che riceve un numero e dice se è pari o dispari.
'''

def pari_dispari(num: int) -> str:
    if num % 2 == 0:
        return "Pari"
    else:
        return "Dispari"

print(pari_dispari(5))
print(pari_dispari(24))