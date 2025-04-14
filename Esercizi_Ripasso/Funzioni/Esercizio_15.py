# Esercizio 15
'''
Scrivere una funzione get_doubles() che possa 
raddoppiare i valori (numeri interi) in una lista.
'''

def get_doubles(my_list:list[int]) ->list[int]:

    my_list_copy = []

    for num in my_list:
        num = num * 2
        my_list_copy.append(num)

    return my_list_copy

print(get_doubles([1, 2, 3, 4, 5]))
