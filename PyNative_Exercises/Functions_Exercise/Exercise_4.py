# Exercise 4: Create a function with a default argument

def show_employee(nome, stipendio:int=9000):
    print(f"Nome: {nome}, Stipendio: {stipendio}")

show_employee("Ben", 12000)
show_employee("Jessa")