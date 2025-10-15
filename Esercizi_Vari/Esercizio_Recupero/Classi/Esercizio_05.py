'''
Esercizio: Sistema di Gestione di un Parco Acquatico
Implementa tre classi interagenti per gestire le prenotazioni degli scivoli acquatici.

1. Classe SlideTicket
Rappresenta un biglietto per accedere a uno scivolo.

A. Attributi:
    * ticket_id: str
    * slide_name: str
    * time_slot: str (es. "10:00-11:00")
    * is_reserved: bool

B. Metodi:
* reserve() -> None
Se is_reserved è False, lo imposta a True; altrimenti stampa:
"Il biglietto per lo scivolo '{self.slide_name}' alle '{self.time_slot}' è già riservato."

* cancel() -> None
Se is_reserved è True, lo imposta a False; altrimenti stampa:
"Il biglietto per lo scivolo '{self.slide_name}' alle '{self.time_slot}' non risulta riservato."


2. Classe Visitor

A. Attributi:
    * visitor_id: str
    * name: str
    * reserved_tickets: list[SlideTicket]

B. Metodi:
* reserve_ticket(ticket: SlideTicket) -> None
Se il biglietto non è riservato, lo aggiunge a reserved_tickets e chiama ticket.reserve().
Altrimenti stampa:
"Il biglietto per lo scivolo '{ticket.slide_name}' non è disponibile."

* cancel_ticket(ticket: SlideTicket) -> None
Se il biglietto è in reserved_tickets, lo rimuove e chiama ticket.cancel().
Altrimenti stampa:
"Il biglietto per lo scivolo '{ticket.slide_name}' non è stato riservato da questo visitatore."

3. Classe WaterPark

A. Attributi:
    * tickets: dict[str, SlideTicket]
    * visitors: dict[str, Visitor]

B. Metodi:
* add_ticket(ticket_id: str, slide_name: str, time_slot: str) -> None
Se ticket_id esiste già, stampa:
"Il biglietto con ID '{ticket_id}' esiste già."
Altrimenti crea e aggiunge un nuovo SlideTicket.

* register_visitor(visitor_id: str, name: str) -> None
Se visitor_id esiste già, stampa:
"Il visitatore con ID '{visitor_id}' è già registrato."
Altrimenti crea e aggiunge un nuovo Visitor.

* reserve_ticket(visitor_id: str, ticket_id: str) -> None
Se entrambi esistono, invoca visitor.reserve_ticket(ticket).
Altrimenti stampa:
"Visitatore o biglietto non trovato."

* cancel_ticket(visitor_id: str, ticket_id: str) -> None
Se entrambi esistono, invoca visitor.cancel_ticket(ticket).
Altrimenti stampa:
"Visitatore o biglietto non trovato."

* list_available_tickets() -> list[str]
Restituisce una lista di ticket_id non riservati.

* list_visitor_reservations(visitor_id: str) -> list[str] | str
Se il visitatore esiste, restituisce una lista di ticket_id riservati.
Altrimenti restituisce:
"Errore: visitatore non trovato."
'''

class SlideTicket:
    def __init__(self, ticket_id: str, slide_name: str, time_slot: str):
        self.ticket_id = ticket_id
        self.slide_name = slide_name
        self.time_slot = time_slot
        self.is_reserved: bool = False
    
    def reserve(self) -> None:
        if not self.is_reserved:
            self.is_reserved = True

        else:
            print(f"Il biglietto per lo scivolo '{self.slide_name}' alle '{self.time_slot}' è già riservato")
    
    def cancel(self) -> None:
        if self.is_reserved:
            self.is_reserved = False
        else:
            print(f"Il biglietto per lo scivolo '{self.slide_name}' alle '{self.time_slot}' non risulta riservato")

class Visitor:
    def __init__(self, visitor_id: str, name: str):
        self.visitor_id = visitor_id
        self.name = name
        self.reserved_tickets: list[SlideTicket] = []
    
    def reserve_ticket(self, ticket: SlideTicket) -> None:
        if ticket not in self.reserved_tickets:
            self.reserved_tickets.append(ticket)
            ticket.reserve()
        else:
            print(f"Il biglietto per lo scivolo '{ticket.slide_name}' non è disponibile")
    
    def cancel_ticket(self, ticket: SlideTicket) -> None:
        if ticket in self.reserved_tickets:
            self.reserved_tickets.remove(ticket)
            ticket.cancel()
        else:
            print(f"Il biglietto per lo scivolo '{ticket.slide_name}' non è stato riservato da questo visitatore")

class WaterPark:
    def __init__(self):
        self.tickets: dict[str, SlideTicket] = {}
        self.visitors: dict[str, Visitor] = {}
    
    def add_ticket(self, ticket_id: str, slide_name: str, time_slot: str) -> None:
        if ticket_id in self.tickets:
            print(f"Il biglietto con ID {ticket_id} esiste già")
        else:
            self.tickets[ticket_id] = SlideTicket(ticket_id, slide_name, time_slot)
    
    def register_visitor(self, visitor_id: str, name: str) -> None:
        if visitor_id in self.visitors:
            print(f"Il visitatore ID {visitor_id} è già registrato")
        else:
            self.visitors[visitor_id] = Visitor(visitor_id, name)
    
    def reserve_ticket(self, visitor_id: str, ticket_id: str) -> None:
        if visitor_id  not in self.visitors or ticket_id not in self.tickets:
            print("Visitatore o biglietto non trovato")

        else:    
            visitor = self.visitors[visitor_id]
            ticket = self.tickets[ticket_id]

            return visitor.reserve_ticket(ticket)

    def cancel_ticket(self, visitor_id: str, ticket_id: str) -> None:
        if visitor_id not in self.visitors or ticket_id not in self.tickets:
            print("Visitatore o biglietto non trovato")
        
        else:
            visitor = self.visitors[visitor_id]
            ticket = self.tickets[ticket_id]

            return visitor.cancel_ticket(ticket)

    def list_available_tickets(self) -> list[str]:
        return [t_id for t_id, ticket in self.tickets.items() if not ticket.is_reserved]
    
    def list_visitor_reservation(self, visitor_id: str) -> list[str]|str:
        if visitor_id in self.visitors:
            visitor = self.visitors[visitor_id]
            return [ticket.ticket_id for ticket in visitor.reserved_tickets]
        else:
            print("Errore: visitatore non trovato")
            