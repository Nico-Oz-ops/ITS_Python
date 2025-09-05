'''
Esercizio 7 - Operazioni matematiche

Tema: Polimorfismo + funzioni di ordine superiore
Obiettivo: Applicare polimorfismo in un contesto matematico per eseguire operazioni diverse su una coppia di numeri.

Traccia:

1. Definisci una superclasse astratta Operazione con un metodo astratto calcola(a, b).

    * a e b sono due numeri su cui eseguire l’operazione.

2. Crea quattro sottoclassi che ereditano da Operazione:

    * Somma → restituisce la somma di a e b.
    * Sottrazione → restituisce la differenza a - b.
    * Moltiplicazione → restituisce il prodotto a * b.
    * Divisione → restituisce il quoziente a / b.

3. Crea una lista di operazioni, contenente oggetti di tipo Somma, Sottrazione, Moltiplicazione e Divisione.

4. Applica tutte le operazioni alla stessa coppia di numeri usando un unico ciclo for, 
   e stampa il risultato di ciascuna operazione con un messaggio chiaro.
'''

from abc import ABC, abstractmethod 

class Operazione(ABC):
    @abstractmethod
    def calcola(self, a: int, b: int):
        pass

class Somma(Operazione):
    def calcola(self, a, b):
        return a + b

class Sottrazione(Operazione):
    def calcola(self, a, b):
        return a - b

class Moltiplicazione(Operazione):
    def calcola(self, a, b):
        return a * b

class Divisione(Operazione):
    def calcola(self, a, b):
        if b == 0:
            raise ValueError("Errore, non si può dividere per zero.")
        return a / b

operazioni = [
    Somma(),
    Sottrazione(),
    Moltiplicazione(),
    Divisione()
]
a = 5
b = 8

for operazione in operazioni:
    print(f"{operazione.__class__.__name__}: {operazione.calcola(a, b):.2f}")

# Un'altra versione
class Operazione(ABC):
    @abstractmethod
    def calcola(self):
        pass

class Somma(Operazione):
    def __init__(self, a: int, b: int):
        super().__init__()
        self.a = a
        self.b = b
    
    def calcola(self):
        return self.a + self.b

class Sottrazione(Operazione):
    def __init__(self, a: int, b: int):
        super().__init__()
        self.a = a
        self.b = b
    
    def calcola(self):
        return self.a - self.b

class Moltiplicazione(Operazione):
    def __init__(self, a: int, b: int):
        super().__init__()
        self.a = a
        self.b = b
    
    def calcola(self):
        return self.a * self.b

class Divisione(Operazione):
    def __init__(self, a: int, b: int):
        super().__init__()
        self.a = a
        self.b = b
    
    def calcola(self):
        if self.b == 0:
            raise ValueError("Errore, non si può dividere per zero")
        return self.a / self.b

operazioni = [
    Somma(4, 7),
    Sottrazione(9, 3),
    Moltiplicazione(8, 12),
    Divisione(85, 7)
]

for op in operazioni:
    print(f"{op.__class__.__name__}: {op.calcola():.1f}")