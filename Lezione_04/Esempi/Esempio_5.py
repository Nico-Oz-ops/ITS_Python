# 5 - Definire una funzione che ritorni una lista

def get_coordinates() -> list[float]:
    return [12.5, 45.8]

coords = get_coordinates()
print(coords[0], coords[1], sep=", ")


def get_coordinates() -> list[float]:
    return[float(input("Inserire le coordenate: ")), float(input("Inserire le coordenate: "))]

coords = get_coordinates()
print(coords[0], coords[1], sep=", ")

