# Esercizio 4
'''Write a function check_each(), which takes a list of numbers as argument.
Using a for loop, iterate through the list.
For each number, print “bigger” if it’s bigger than 5, 
“smaller” if it’s smaller than 5, and “equal” if it’s equal to 5.'''

def check_each(numbers) -> list[float]:
    for number in numbers:
        if number > 5:
            print(f"{number} è maggiore di 5.")
        elif number < 5:
            print(f"{number} è minore di 5.")
        else:
            print(f"{number} è uguale a 5.")

check_each([2, 8, 16, 5, 2.65, 5.5, 0.78])