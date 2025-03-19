# Exercise 1: Create a function in Python

# Opzione 1
def name_and_age(name, age):
    nome = name
    età = age

    return name, age

nome, età = name_and_age(input("Inserire un nome: "), int(input("Inserire l'età: ")))

print(f"{nome} ha {età} anni") 


# Opzione 2
def nome_eta(name, age):
    print(name, age)
   
nome_eta("Nico", 27)
