# Esercizio 04 - Controllo della parità di un numero

# n = float(input("Inserire un numero: "))

# if n % 2 == 0:
#     print(f"Il numero inserito \"{n}\" è pari")
# else:
#     print(f"Il numero inserito \"{n}\" è dispari")


while True:
    n = float(input("Inserire un numero: "))
    if n == "stoppi":
        break
    if n % 2 == 0:
        print(f"Il numero inserito \"{n}\" è pari")
    else:
        print(f"Il numero inserito \"{n}\" è dispari")