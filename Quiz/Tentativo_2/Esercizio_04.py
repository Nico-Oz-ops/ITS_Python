# Esercizio 04
'''Il codice dovrebbe stampare i numeri all'interno di una lista.'''

# Opzione 1
numbers:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9] 

for number in numbers:
    print(f"Number: {number}")


# Opzione 2
numbers = []

for number in range(1, 9 + 1):
    numbers.append(number)
    print(f"Number: {number}")

print(numbers)

