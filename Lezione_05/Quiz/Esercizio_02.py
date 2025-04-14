# Esercizio 02
'''
Hai una lista di numeri interi. Il tuo compito è riorganizzare questa lista in modo che:
tutti i numeri pari vengano prima di tutti i numeri dispari;
l’ordine relativo tra pari e dispari va mantenuto;
l’obiettivo è solo separare i pari dai dispari, con i pari che vengono per primi.
'''

def even_odd_pattern(numbers:list[int]) -> list[int]:

    numeri_pari = []
    numeri_dispari = []

    for number in numbers:
        if number % 2 == 0:
            numeri_pari.append(number)

        else:
            numeri_dispari.append(number)
    
    return numeri_pari + numeri_dispari 

print(even_odd_pattern([3, 6, 1, 8, 4, 7]))

