# Exercise 7: Assegna un nome diverso alla funzione e chiamala tramite il nuovo nome

def display_student(name:str, age:int):
    print(name, age, sep=", ")

display_student("Nico", 36)

show_student = display_student
show_student("Javi", 35)

new_student = display_student
new_student("Lisa", 27)
