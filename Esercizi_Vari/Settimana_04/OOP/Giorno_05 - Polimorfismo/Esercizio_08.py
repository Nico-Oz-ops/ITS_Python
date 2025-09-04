'''
Esercizio 8 - Mezzi di trasporto speciali

Tema: Polimorfismo e override in un contesto leggermente più complesso.
Obiettivo: Creare più classi di veicoli con metodi diversi per calcolare 
velocità o autonomia, e usare una lista polimorfica per stampare i risultati.

Traccia:
    * Crea una classe base VeicoloSpeciale con attributi marca e modello, 
    e un metodo autonomia() che restituisce 0 (metodo da override).

Sottoclassi:

    * AutoElettrica → aggiungi capacita_batteria (kWh) e consumo (kWh/100km). 
        Override autonomia() = capacità / consumo x 100.

    * MotoBenzina → aggiungi serbatoio (litri) e consumo (l/100km). 
        Override autonomia() = serbatoio / consumo x 100.

    * Camion → aggiungi serbatoio e consumo, ma autonomia ridotta del 20% per peso extra.

    * Crea una lista di veicoli misti e stampa marca, modello e autonomia di ciascuno usando un unico loop.

Suggerimento: qui il polimorfismo si vede quando chiami autonomia() su tutti i tipi di veicolo, 
senza preoccuparti di quale sia il tipo concreto.
'''