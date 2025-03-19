# Exercise 2: Create a function with variable length of arguments

def func1(*args):
    for i in args:
        print(f"Gli elementi sono: {i}")
        

func1(15, 20, 35, "str", 3.25, True)



def func1(*args):
    risultato = []
    for i in args:
        risultato.append(i)
    return risultato
        

lolo = func1(15, 20, 35, "str", 3.25, True)
print(lolo)