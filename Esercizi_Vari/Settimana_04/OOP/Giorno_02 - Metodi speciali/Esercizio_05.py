'''
5. Oggetto “stampabile”

Tema: Metodi speciali - __repr__
Obiettivo: Fornire una rappresentazione utile per il debug.

Nome dell’esercizio: Prodotto

Traccia:
Crea una classe Prodotto con attributi nome e prezzo. Implementa sia __str__ che __repr__.

    * __str__ → output leggibile per l’utente (es. "Prodotto: Laptop - Prezzo: 1200€")
    * __repr__ → output più tecnico per il debug (es. "Prodotto('Laptop', 1200)").

Suggerimento: In __repr__ restituisci la stringa come se fosse un “codice Python” ricreabile.
'''

class Prodotto:
    def __init__(self, nome: str, prezzo: float):
        self.nome = nome
        self.prezzo = prezzo
    
    def __str__(self):
        return f"Prodotto: {self.nome}, Prezzo: {self.prezzo}"

    def __repr__(self):
        return f"Prodotto({self.nome}, {self.prezzo})"
    
prodotto1 = Prodotto("Avena", 0.95)
prodotto2 = Prodotto("Latte", 0.99)

print(prodotto1)
print([prodotto2])
        