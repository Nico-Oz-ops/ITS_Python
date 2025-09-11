'''
Esercizio 3 - Rettangolo con più proprietà collegate

Traccia:

1. Crea una classe Rettangolo con attributi protetti _larghezza e _altezza.

2. Esporre larghezza e altezza tramite @property e setter con validazione (devono essere >0).

3. Aggiungi proprietà calcolate area e perimetro (solo getter).

4. Dimostra l’uso creando un rettangolo, stampando area e perimetro, e aggiornando larghezza o altezza.
'''
class Rettangolo:
    def __init__(self, larghezza: float, altezza: float):
        self.larghezza = larghezza # usa il setter
        self.altezza = altezza # usa il setter
    
    @property
    def larghezza(self):
        return self._larghezza
    
    @larghezza.setter
    def larghezza(self, larghezza: float):
        if not isinstance(larghezza, (int, float)) or larghezza < 0:
            raise ValueError("Valore di larghezza non valido")
        self._larghezza = larghezza
    
    @property
    def altezza(self):
        return self._altezza

    @altezza.setter
    def altezza(self, altezza: float):
        if not isinstance(altezza, (int, float)) or altezza < 0:
            raise ValueError("Valore di altezza non valido")
        self._altezza = altezza
    
    @property
    def perimetro(self):
        return 2 * (self._larghezza + self._altezza)
    
    @property
    def area(self):
        return self._larghezza * self._altezza
    
    def __str__(self):
        return f"Caratteristiche del rettangolo {self._larghezza} x {self._altezza}:\nArea: {self.area}\nPerimetro: {self.perimetro}"

rettangolo = Rettangolo(5.5, 6)
print(rettangolo)

# Osservazione importante !!!

# Nell'__init__ assegno tramite i setter invece di _larghezza e _altezza direttamente, 
# così la validazione viene applicata subito anche alla creazione dell’oggetto

# In questo modo evito che qualcuno possa creare un rettangolo con 
# valori invalidi direttamente nell’inizializzazione.