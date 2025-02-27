# Opzione 1

# list_animals = ["dog", "cow", "horse"]

# print(f"A {list_animals[0]} would make a great pet")
# print(f"A {list_animals[1]} is a beatiful animal")
# print(f"A {list_animals[-1]} is a great animal to ride")
# print("All of these animals are mammals")

# Opzione 2 - Ciclo For

# list_animals_2 = ["dog", "cow", "horse"]
# for animal in list_animals_2:
#     print(animal)
#     print(f"A {animal} would make a great pet")

# Opzione 3 - Ciclo While

# lista_animale = []
# i = 1

# while i <= 5:
#     animale = input("Inserire il nome di un animale: ")
#     lista_animale.append(animale)
#     i += 1
#     print(f"Animale: {animale}")
# print(f"Gli animali scelti sono: {lista_animale}")


#  Opzione 4 - Ciclo While: True

lista_animale_2 = []

while True:
    animale = input("Inserire il nome di un animale: ")
    if animale == "stopi":
        break

    lista_animale_2.append(animale)

    print(f"Hai scelto l'animale: {animale}!")
print(f"Gli animali scelti sono: {lista_animale_2}")




