'''
Esercizio 10 - Veicolo

Tema: Incapsulamento e aggiornamento sicuro

Crea una classe Veicolo con:

    * __modello (stringa)
    * __marca (stringa)
    * __chilometri (float ≥0)

Metodi:

    * Getter/setter con validazioni
    * guida(km) → aggiunge km percorsi (non può essere negativo)
    * __str__()
'''
class Veicolo:
    def __init__(self, modello: str, marca: str, chilometri: float):
        self.set_modello(modello)
        self.set_marca(marca)
        self.set_chilometri(chilometri)
    
    def get_modello(self) -> str:
        return self.__modello
    
    def get_marca(self) -> str:
        return self.__marca
    
    def get_chilometri(self) -> float:
        return self.__chilometri
    
    def set_modello(self, modello: str):
        if not isinstance(modello, str) or modello.strip() == "":
            raise ValueError(f"Errore, modello '{modello}' non valido.")
        self.__modello = modello
    
    def set_marca(self, marca: str):
        if not isinstance(marca, str) or marca.strip() == "":
            raise ValueError(f"Errore, marca '{marca}' non valida.")
        self.__marca = marca
    
    def set_chilometri(self, chilometri: float):
        if not isinstance(chilometri, (int, float)) or chilometri < 0:
            raise ValueError(f"Errore, chilometri inseriti '{chilometri}' non validi.")
        self.__chilometri = chilometri
    
    def guida(self, km_percorsi: float):
        if not isinstance(km_percorsi, (int, float)) or km_percorsi < 0:
            raise ValueError("Errore, il numero di chilometri percorsi inseriti non è valido.")
        self.__chilometri += km_percorsi
    
    def __str__(self):
        return f"Modello: {self.__modello}\nMarca: {self.__marca}\nChilometri: {self.__chilometri:.2f}"

veicolo = Veicolo("911", "Porsche", 10565.75)
print(veicolo)

print("-" * 50)

veicolo.guida(1245.36)
print(veicolo)

print("-" * 50)

veicolo.guida(0.1)
print(veicolo)

print("-" * 50)

veicolo.guida(-25) # scatta l'errore
print(veicolo)     