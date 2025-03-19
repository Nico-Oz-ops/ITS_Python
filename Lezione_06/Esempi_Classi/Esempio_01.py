# class MiaLista:
#     """docstring for MiaLista"""
#     def __init__(self):
#         self.lst: list[int] = []
    
#     def aggiungi(self, val: int):
#         self.lst.append(val)
    
#     def rimuovi(self, val):
#         if val in self.lst:
#             self.lst.remove(val)
    
#     def __repr__(self):
#         return f"{self.lst}"

# mylist = MiaLista()

# mylist.aggiungi(10)

# mylist.aggiungi(11)

# mylist.rimuovi(10)

# print(mylist)

# print("-" * 50)


# class Persona:
#     def __init__(self, age: int = 100, name="Pippo"):
#         self.age = age
#         self.name = name
    
#     def print_age(self):
#         print(self.age)

# p = Persona()
# # p.print_age()
# print(p)

# print("-" * 50)

# Esempio 3

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name: {self.name}, age: {self.age} anni)"

nico = Person("Nico V.", 36)
lulù = Person("Lulù J.", 29)

print(nico, lulù)

# Esempio 4

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} anni"

nico = Person("Nico V.", 36)
lulù = Person("Lulù J.", 29)

print(nico)
print(lulù)

# Esempio 5

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_name_age(self):
        print(self.name, self.age)

nico = Person("Nico V.", 36)

print(nico)



