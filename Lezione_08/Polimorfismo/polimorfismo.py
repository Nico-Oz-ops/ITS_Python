from persona import Persona
from alieno import Alieno   

# creare un oggetto p della classe Persona
p: Persona = Persona("Nico", "Rojas", 37)
print(p)

# creare un oggetto et della classe Alieno
et: Alieno = Alieno("Andromeda")
print(et)

# l'oggetto 'p' invoca il metodo speak()
p.speak()

# l'oggetto 'et' invoca il metodo speak()
et.speak()


