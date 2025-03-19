# Esercizio 5
'''Write a function add_one(). It takes an integer as argument. 
The function adds 1 to the integer and returns it.
Write another function add_one_to_list(). It takes a list of integers as argument.
Define a variable new_list in this function.
Using a for loop, iterate through the argument list.
Using add_one(), fill new_list with integers from the argument list incremented by 1.
Print new_list.
Example:
add_one_to_list([1, 2, 3])
>>> [2, 3, 4]'''

def add_one(intero):
    intero += 1
    return intero

def add_one_to_list(lista_interi) -> list[int]:
    new_list = []
    for elemento in lista_interi:
        new_list.append(add_one(elemento))
    print(new_list)

add_one_to_list([75, 95, 36])