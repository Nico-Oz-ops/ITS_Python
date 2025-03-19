# Esercizio 01 - Matching con oggetti (Pattern Matching con classi)
'''Supponiamo di avere una classe Animale e due sottoclassi Cane e Gatto. 
Scrivi un esempio di match per identificare quale tipo di animale è'''

class Animale:
    pass

class Cane(Animale):
    pass

class Gatto(Animale):
    pass

def tipo_animale(animale:str):
    match animale:
        case Cane():
            return "È un cane"
        case Gatto():
            return "È un gatto"
        case _:
            return "È un altro animale"

cane = Cane()
gatto = Gatto()
altro_animale = Animale()

print(tipo_animale(cane))
print(tipo_animale(gatto))
print(tipo_animale(altro_animale))