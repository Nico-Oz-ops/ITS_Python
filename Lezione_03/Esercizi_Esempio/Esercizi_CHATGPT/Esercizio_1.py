# 1 - Controllare se un numero è positivo, negativo o zero

numero = float(input("Inserire un numero: "))

match numero:
    case numero if numero > 0:
        print(f"Il {numero} è positivo")
    case numero if numero < 0:
        print(f"Il {numero} è negativo")
    case _:
        print(f"Il numero {numero} è uguale a zero")