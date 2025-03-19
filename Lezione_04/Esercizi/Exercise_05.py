# Exercise 5

def add_one(num:int):
    num += 1
    return num
    

def add_one_to_list(lista):
    new_list = []
    for elemento in lista:
        new_list.append(add_one(elemento))
    print(new_list)

add_one_to_list([1, 2, 3])
