'''
Esercizio 3 - Sistema di gestione veicoli

Obiettivo: Applicare classi astratte per creare una gerarchia più realistica e polimorfica.

Nome dell’esercizio: Veicolo

Traccia:

Crea una classe astratta Veicolo con:

* attributi: marca, modello, anno
* metodi astratti: avvia(), ferma(), descrizione()

Crea tre sottoclassi:

* Auto
* Moto
* Camion

Ognuna deve implementare i tre metodi astratti con messaggi personalizzati 
(es. "L’auto Toyota Corolla è partita.").

Crea una lista di veicoli diversi e scrivi una funzione che li avvii tutti 
e poi li fermi tutti, usando solo metodi della classe base.

Suggerimento: usa il polimorfismo: non serve controllare il tipo di veicolo.
'''

from abc import ABC, abstractmethod

class Veicolo(ABC):
    def __init__(self, marca: str, modello: str, anno: int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    @abstractmethod
    def avvia(self):
        pass

    @abstractmethod
    def ferma(self):
        pass

    @abstractmethod
    def descrizione(self):
        pass

class Auto(Veicolo):
    def avvia(self):
        print(f"L'auto {self.marca} {self.modello} è partita")
    
    def ferma(self):
        print(f"L'auto {self.marca} {self.modello} si è fermata")
    
    def descrizione(self):
        print(f"Info dell'auto\nMarca: {self.marca}\nModello: {self.modello}\nAnno: {self.anno}")


class Moto(Veicolo):
    def avvia(self):
        print(f"La moto {self.marca} {self.modello} è partita")
    
    def ferma(self):
        print(f"La moto {self.marca} {self.modello} si è fermata")
    
    def descrizione(self):
        print(f"Info della moto\nMarca: {self.marca}\nModello: {self.modello}\nAnno: {self.anno}")

class Camion(Veicolo):
    def avvia(self):
        print(f"Il camion {self.marca} {self.modello} è partito")
    
    def ferma(self):
        print(f"Il camion {self.marca} {self.modello} si è fermato")
    
    def descrizione(self):
        print(f"Info del camion\nMarca: {self.marca}\nModello: {self.modello}\nAnno: {self.anno}")

def gestione_veicoli(lista_veicoli: list[Veicolo]):
    print("Avvio di tutti i veicoli!!\n")

    for v in lista_veicoli:
        v.avvia()
    
    print("\nArresto di tutti i veicoli!!\n")

    for v in lista_veicoli:
        v.ferma()

veicoli = [
    Auto("Toyota", "Corolla", 2020),
    Moto("Ducati", "Monster 821", 2021),
    Camion("Volvo", "FH16", 2018)
    ]

print("== Descrizione dei veicoli ==")
for v in veicoli:
    v.descrizione()
print("---------------------")


gestione_veicoli(veicoli)