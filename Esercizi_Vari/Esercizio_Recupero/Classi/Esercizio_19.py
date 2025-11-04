'''
Esercizio: Sistema di Gestione di una Società di Car Sharing

Implementa tre classi interagenti per gestire il noleggio e la restituzione dei veicoli.

1. Classe VehicleRental
Rappresenta un singolo noleggio di un veicolo.

A. Attributi:
    * rental_id: str
    * vehicle_model: str
    * return_date: str (es. "2025-12-05")
    * is_rented: bool

B. Metodi:
* rent() -> None
Se is_rented è False, lo imposta a True; altrimenti stampa:
"Il veicolo '{self.vehicle_model}' è già noleggiato."

* return_vehicle() -> None
Se is_rented è True, lo imposta a False; altrimenti stampa:
"Il veicolo '{self.vehicle_model}' non risulta attualmente noleggiato."


2. Classe Customer

A. Attributi:
    * customer_id: str
    * name: str
    * active_rentals: list[VehicleRental]

B. Metodi:
* rent_vehicle(rental: VehicleRental) -> None
Se il veicolo non è già noleggiato, lo aggiunge a active_rentals e chiama rental.rent().
Altrimenti stampa:
"Il veicolo '{rental.vehicle_model}' non è disponibile per il noleggio."

* return_vehicle(rental: VehicleRental) -> None
Se il veicolo è in active_rentals, lo rimuove e chiama rental.return_vehicle().
Altrimenti stampa:
"Il veicolo '{rental.vehicle_model}' non risulta tra i noleggi attivi del cliente."


3. Classe CarSharingSystem

A. Attributi:
    * rentals: dict[str, VehicleRental]
    * customers: dict[str, Customer]

B. Metodi:
* add_rental(rental_id: str, vehicle_model: str, return_date: str) -> None
Se rental_id esiste già, stampa:
"Il noleggio con ID '{rental_id}' esiste già."
Altrimenti crea e aggiunge un nuovo VehicleRental.

* register_customer(customer_id: str, name: str) -> None
Se customer_id esiste già, stampa:
"Il cliente con ID '{customer_id}' è già registrato."
Altrimenti crea e aggiunge un nuovo Customer.

* rent_vehicle(customer_id: str, rental_id: str) -> None
Se entrambi esistono, invoca customer.rent_vehicle(rental).
Altrimenti stampa:
"Cliente o noleggio non trovato."

* return_vehicle(customer_id: str, rental_id: str) -> None
Se entrambi esistono, invoca customer.return_vehicle(rental).
Altrimenti stampa:
"Cliente o noleggio non trovato."

* list_available_vehicles() -> list[str]
Restituisce una lista di rental_id dei veicoli non ancora noleggiati.

* list_customer_rentals(customer_id: str) -> list[str] | str
Se il cliente esiste, restituisce una lista di rental_id attivi.
Altrimenti restituisce:
"Errore: cliente non trovato."
'''