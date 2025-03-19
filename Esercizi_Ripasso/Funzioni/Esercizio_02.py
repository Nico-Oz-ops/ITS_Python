# Esercizio 2
'''Write a function check_length(), which takes a string as an argument.
Using if / else, check if the length of the string is bigger, smaller, or equal to 10 characters.'''

def check_lenght(stringa:str):
    if len(stringa) > 10:
        print(f"{stringa} ha più di 10 caratteri")
    elif len(stringa) < 10:
        print(f"{stringa} ha meno di 10 caratteri")
    else:
        print(f"{stringa} ha 10 caratteri")

check_lenght("\"Paralelepipedo\"")
check_lenght("\"Completo italiano\"")
check_lenght("\"Casita\"")
check_lenght("\"Combosonic\"")