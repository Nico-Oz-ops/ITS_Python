from Animale import Animale

cane:Animale = Animale("Cane", "Labrador", 4, "Marrone")
print(cane.nome, cane.razza, cane.zampe, cane.colore, sep=", ")

print("-" * 50)

from Animale_2 import Animale_2

anl:Animale = Animale_2()

print(anl.displayData())

print("-" * 50)
anl.setName("Cane")
anl.setRace("Pastore Tedesco")
anl.setPaws(5)
anl.setColor("Nero")

print(anl.displayData())
print("-" * 50)

print(anl.getName(), anl.getRace(), anl.getPaws(), anl.getColor())