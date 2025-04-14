# dal file "Esempio_persona.py" importa la classe Persona
from Esempio_persona import Persona

# creare un oggetto di tipo Persona
nv:Persona = Persona("Nicolas", "Valenzuela", 36)

print(nv)
print("-" * 50)

print(nv.name, nv.lastname, nv.age, sep=", ")
print("-" * 50)
        
# dal file Esempio_persona_2.py importa la classe Persona
from Esempio_persona_2 import Persona

nv:Persona = Persona()

# voglio richiamare la funzione displayData della classe persona per stampare in output 
# le informazioni relative alla persona "nv"

nv.displayData()

# impostare il nome della persona "nv"
nv.setName("Nicolas")

print("-" * 50)

nv.displayData()

# impostare il cognome della Persona (la classe) "nv"
nv.setLastname("Valenzuela")

# impostare l'età della persona "nv"
nv.setAge(36)

print("-" * 50)
nv.displayData()

print("-" * 50)

# ritorna i valori della Classe
print(nv.getName(), nv.getLastname(), nv.getAge())

