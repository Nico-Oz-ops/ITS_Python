# Esercizio 14
'''
Creare una funzione per calcolare il 
cuadrato di ogni numero intero di una lista.
'''

def square(numbers:list[int]) -> int:
    new_numbers = []

    for number in numbers:
        new_numbers.append(number ** 2)
    
    return new_numbers

print(square([1, 2, 3, 4, 5, 6]))


