# Esercizio 5
'''La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
Un errore nell'implementazione porta a risultati inaspettati.
Trova l'errore e correggi il codice affinché soddisfi i casi di test.
'''

def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers)/len(numbers)
print(calculate_average([1, 2, 3, 6]))