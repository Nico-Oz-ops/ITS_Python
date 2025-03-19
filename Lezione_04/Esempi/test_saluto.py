# A - import saluto, importa tutto il modulo saluto
import saluto

saluto.greet("Nicolino")

# le posso dare un nickname al nome della funzione, in questo caso da "saluto" a "s"
import saluto as s 
s.greet("Lisa la Buhaiolinas")

# B - se voglio importare solo la funzione greet dal modulo saluto ed ignorare il resto del modulo saluto, farò:
from saluto import greet
greet("Javi")


from saluto import greet as g
g("Cacchina")



def hi(name, saluto="hola"):
    print(f"{name}, {saluto}")

hi("Mike")