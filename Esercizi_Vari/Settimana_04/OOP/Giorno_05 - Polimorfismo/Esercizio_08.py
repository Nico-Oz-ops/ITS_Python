'''
Esercizio 8 - Mezzi di trasporto speciali

Tema: Polimorfismo e override in un contesto leggermente più complesso.
Obiettivo: Creare più classi di veicoli con metodi diversi per calcolare 
velocità o autonomia, e usare una lista polimorfica per stampare i risultati.

Traccia:
1. Crea una classe base VeicoloSpeciale con attributi marca e modello, e un metodo autonomia() 
   che restituisce 0 (metodo da override).

2. Sottoclassi:

    * AutoElettrica → aggiungi capacita_batteria (kWh) e consumo (kWh/100km). 
        Override autonomia() = capacità / consumo x 100.

    * MotoBenzina → aggiungi serbatoio (litri) e consumo (l/100km). 
        Override autonomia() = serbatoio / consumo x 100.

    * Camion → aggiungi serbatoio e consumo, ma autonomia ridotta del 20% per peso extra.

3. Crea una lista di veicoli misti e stampa marca, modello e autonomia di ciascuno usando un unico loop.

Suggerimento: qui il polimorfismo si vede quando chiami autonomia() su tutti i tipi di veicolo, 
senza preoccuparti di quale sia il tipo concreto.
'''

class VeicoloSpeciale:
    def __init__(self, marca: str, modello: str):
        self.marca = marca
        self.modello = modello
    
    def get_marca(self) -> str:
        return self.marca 
    
    def get_modello(self) -> str:
        return self.modello 
    
    def autonomia(self):
        return 0

class AutoElettrica(VeicoloSpeciale):
    def __init__(self, marca, modello, capacita_batteria: int|float, consumo: int|float):
        super().__init__(marca, modello)
        self.set_capacita_batteria(capacita_batteria)
        self.set_consumo(consumo)
    
    def get_capacita_batteria(self) -> int|float:
        return self.capacita_batteria
    
    def get_consumo(self) -> int|float:
        return self.consumo
    
    def set_capacita_batteria(self, capacita_batteria: int|float):
        if not isinstance(capacita_batteria, int|float) or capacita_batteria <= 0:
            raise ValueError("Capacità di batteria non valida")
        self.capacita_batteria = capacita_batteria
    
    def set_consumo(self, consumo: int|float):
        if not isinstance(consumo, int|float) or consumo < 0:
            raise ValueError("Valore di consumo non valido")
        self.consumo = consumo
    
    def autonomia(self) -> int|float:
        return (self.capacita_batteria / self.consumo) * 100
    
class MotoBenzina(VeicoloSpeciale):
    def __init__(self, marca, modello, serbatoio: int|float, consumo: int|float):
        super().__init__(marca, modello)
        self.serbatoio = serbatoio
        self.consumo = consumo
    
    def get_serbatoio(self) -> int|float:
        return self.serbatoio
    
    def get_consumo(self) -> int|float:
        return self.consumo
    
    def set_serbatoio(self, serbatoio: int|float):
        if not isinstance(serbatoio, (int, float)) or serbatoio < 0:
            raise ValueError("Valore di serbatoio non valido")
        self.serbatoio = serbatoio
    
    def set_consumo(self, consumo: int|float):
        if not isinstance(consumo, (int, float)) or consumo < 0:
            raise ValueError("Valore di consumo non valido")
        self.consumo = consumo
    
    def autonomia(self) -> int|float:
        return (self.serbatoio / self.consumo) * 100

class Camion(VeicoloSpeciale):
    def __init__(self, marca, modello, serbatoio: int|float, consumo: int|float):
        super().__init__(marca, modello)
        self.set_serbatoio(serbatoio)
        self.set_consumo(consumo)
    
    def get_serbatoio(self) -> int|float:
        return self.serbatoio 
    
    def get_consumo(self) -> int|float:
        return self.consumo 
    
    def set_serbatoio(self, serbatoio: int|float):
        if not isinstance(serbatoio, (int, float)) or serbatoio < 0:
            raise ValueError("Valore di serbatoio non valido")
        self.serbatoio = serbatoio
    
    def set_consumo(self, consumo: int|float):
        if not isinstance(consumo, (int, float)) or consumo < 0:
            raise ValueError("Valore di consumo non valido")
        self.consumo = consumo
    
    def autonomia(self) -> int|float:
        return (self.serbatoio / self.consumo) * 100 * 0.8

veicoli = [AutoElettrica("Tesla", "Model 3", 75, 15),
           MotoBenzina("Yamaha", "MT-07", 14, 5),
           Camion("Volvo", "FH16", 400, 30)
           ]

for veicolo in veicoli:
    print(f"Marca: {veicolo.get_marca()} | Modello: {veicolo.get_modello()} | Autonomia: {veicolo.autonomia():.2f}")

