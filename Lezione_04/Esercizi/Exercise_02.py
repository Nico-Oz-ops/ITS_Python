# Exercise 2

def check_lenght(stringa):
    if len(stringa) > 10:
        print(f" La stringa \"{stringa}\" ha più di 10 caratteri")
    elif len(stringa) < 10:
        print(f" La stringa \"{stringa}\" ha meno di 10 caratteri")
    else:
        print(f" La stringa \"{stringa}\" ha 10 caratteri")

check_lenght(input("Inserire una stringa: "))