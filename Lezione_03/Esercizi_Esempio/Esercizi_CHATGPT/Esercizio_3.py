# Identificare la grandezza di una lista

lista = []

while True:
    elemento = input("Inserire un elemento: ")
    if elemento == "stopi":
        break
    
    lista.append(elemento)

match len(lista):
    case 0:
        print("La lista è vuota")
    case 1:
        print(f"La lista ha 1 elemento")
    case 2:
        print(f"La lista ha 2 elementi")
    case 3:
        print(f"La lista ha 3 elementi")
    case _:
        print(f"La lista ha {len(lista)} elementi")
    
