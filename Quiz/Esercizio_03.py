# Esercizio 3 - 
'''Scrivi una funzione che calcola la media di una 
lista di numeri e ritorna il valore arrotondato all'intero più vicino.'''

# def rounded_average(numbers:list[int]) -> int:
#     numbers = []
#     somma = 0
#     for number in numbers:
#         numbers.append(number)
#         somma += number

#     media = somma / len(numbers) if len(numbers) > 0 else 0

#     return media 

# media_num = rounded_average([1, 1, 2, 2])
# print(media_num)



def rounded_average(number:list[int]) -> int:
    media = sum(number)/len(number)
    return round(media)

print(rounded_average([1, 1, 2, 2]))

    


    

