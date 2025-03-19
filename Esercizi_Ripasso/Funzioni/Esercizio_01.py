# Esercizio 01 
''' Write a function check_value(), which takes a number as an argument.
Using if / else, the function should print whether the number is bigger, smaller, or equal to 5'''

def check_value(number:int):
    if number > 5:
        print(f"{number} è maggiore di 5")
    elif number < 5:
        print(f"{number} è minore di 5")
    else:
        print(f"{number} è uguale a 5")

check_value(16)
check_value(4)
check_value(5)