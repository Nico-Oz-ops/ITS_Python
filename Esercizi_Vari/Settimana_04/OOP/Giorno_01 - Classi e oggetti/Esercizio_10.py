'''
Tema: Metodi che modificano attributi
Obiettivo: Aggiornare informazioni interne

Nome: Libro con sconto

Traccia:
Crea una classe Libro con attributi titolo, autore e prezzo.
Aggiungi un metodo applica_sconto(percentuale) che riduce il prezzo del libro della percentuale indicata.
Crea un libro, applica uno sconto del 20% e stampa il prezzo aggiornato.
'''
class Libro:

    def __init__(self, titolo: str, autore: str, prezzo: float):
        self.titolo = titolo
        self.autore = autore
        self.prezzo = prezzo
    
    def applica_sconto(self, percentuale: float):
        self.prezzo -= (self.prezzo * percentuale) # oppure self.prezzo = self.prezzo - (self.prezzo * percentuale)

    def mostra_libro(self):
        return f"Il libro '{self.titolo}' dell'autore '{self.autore}' è scontato del 20%, perciò ${self.prezzo: .2f}"

libro1 = Libro("Cent'anni di solitudine", "Gabriel Garcìa Màrquez", 20)
print(libro1.mostra_libro()) # stampa prezzo normale, senza sconto del 20%
libro1.applica_sconto(0.2)
print(libro1.mostra_libro())# stampa con lo sconto del 20%
