# Exercise 1

def check_value(numero):
    if numero > 5:
        print(f"{numero} è più grande di 5")
    elif numero < 5:
        print(f"{numero} è minore di 5")
    else:
        print(f"{numero} è uguale a 5")

check_value(int(input("Inserire un numero intero: ")))
