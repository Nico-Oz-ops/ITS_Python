# Esercizio 05
'''La funzione dovrebbe calcolare la media dei numeri in una lista di interi.'''

# Opzione 1
def calculate_average(numbers: list[int]) -> float:

    if numbers == 0 or numbers == []:
        return 0
    
    else:
        media_numeri = sum(numbers) / len(numbers)
        return media_numeri



print(f"La media dei numeri è: {calculate_average([1, 2, 3, 4, 5])}")
print(f"La media dei numeri è: {calculate_average([])}")
print("-" * 30)

# Opzione 2
def calculate_average(numbers:list[int]) -> float:

    if len(numbers) == 0:
        return 0
    
    else:
        media = sum(numbers) / len(numbers)
        return media

print(f"La media dei numeri è: {calculate_average([8, 4, 15, 4, 5])}")
print(f"La media dei numeri è: {calculate_average([2, 9, 11, 5])}")
print(f"La media dei numeri è: {calculate_average([0])}")
print(f"La media dei numeri è: {calculate_average([])}")



