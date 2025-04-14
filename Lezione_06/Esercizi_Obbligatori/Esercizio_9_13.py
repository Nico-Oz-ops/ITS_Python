# Esercizio 9.13
'''
Dadi: crea una classe Die con un attributo chiamato sides, che ha un valore predefinito di 6. 
Scrivi un metodo chiamato roll_die() che stampa un numero casuale tra 1 e il numero di lati del dado. 
Crea un dado a 6 facce e lancialo 10 volte. Crea un dado a 10 facce e un dado a 20 facce. Lancia ogni dado 10 volte.
'''
import random

class Die:

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return random.randint(1, self.sides)

# Dado a 6 facce
dado_6 = Die()

print("Lancio del dado a 6 facce:")
for dado in range(10):
    print(dado_6.roll_die())

# Dado a 10 facce
dado_10 = Die()

print("Lancio del dado a 10 facce:")
for dado in range(10):
    print(dado_10.roll_die())

# Dado di 20 facce
dado_20 = Die()

print("Lancio del dado a 20 facce")
for dado in range(10):
    print(dado_20.roll_die())



        