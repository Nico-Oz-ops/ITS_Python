'''
Esercizio: Sistema di Gestione di un Hotel

Implementa tre classi interagenti per gestire le prenotazioni delle camere in un hotel.

1. Classe RoomBooking

Rappresenta una prenotazione per una camera d’hotel.

Attributi:

    * booking_id: str
    * room_number: int
    * date_range: str (es. "2025-07-10 / 2025-07-12")
    * is_booked: bool

Metodi:

* book() -> None
Se is_booked è False, la imposta a True;
altrimenti stampa:
"La camera {self.room_number} per il periodo {self.date_range} è già prenotata."

* cancel() -> None
Se is_booked è True, la imposta a False;
altrimenti stampa:
"La prenotazione per la camera {self.room_number} non risulta attiva."

2. Classe Guest

Rappresenta un cliente dell’hotel.

Attributi:

    * guest_id: str
    * name: str
    * bookings: list[RoomBooking]

Metodi:

* book_room(booking: RoomBooking) -> None
Se la camera non è già prenotata, aggiunge la prenotazione a bookings e chiama booking.book().
Altrimenti stampa:
"La camera {booking.room_number} non è disponibile per il periodo richiesto."

* cancel_booking(booking: RoomBooking) -> None
Se il booking è presente in bookings, lo rimuove e chiama booking.cancel().
Altrimenti stampa:
"La prenotazione per la camera {booking.room_number} non è stata trovata tra quelle del cliente."

3. Classe Hotel

Gestisce tutti i clienti e le prenotazioni.

Attributi:

    * bookings: dict[str, RoomBooking]
    * guests: dict[str, Guest]

Metodi:

* add_booking(booking_id: str, room_number: int, date_range: str) -> None
Se booking_id esiste già, stampa:
"La prenotazione con ID '{booking_id}' esiste già."
Altrimenti crea e aggiunge un nuovo RoomBooking.

* register_guest(guest_id: str, name: str) -> None
Se guest_id esiste già, stampa:
"Il cliente con ID '{guest_id}' è già registrato."
Altrimenti crea e aggiunge un nuovo Guest.

* book_room(guest_id: str, booking_id: str) -> None
Se entrambi esistono, invoca guest.book_room(booking);
altrimenti stampa:
"Cliente o prenotazione non trovata."

* cancel_room(guest_id: str, booking_id: str) -> None
Se entrambi esistono, invoca guest.cancel_booking(booking);
altrimenti stampa:
"Cliente o prenotazione non trovata."

* list_available_rooms() -> list[str]
Restituisce una lista di booking_id non ancora prenotati.

* list_guest_bookings(guest_id: str) -> list[str] | str
Se il cliente esiste, restituisce una lista di booking_id prenotati.
Altrimenti:
"Errore: cliente non trovato."
'''

class RoomBooking:
    def __init__(self, booking_id: str, room_number: int, date_range: str) -> None:
        self.booking_id = booking_id
        self.room_number = room_number
        self.date_range = date_range
        self.is_booked: bool = False
    
    def book(self) -> None:
        if not self.is_booked:
            self.is_booked = True

        else:
            print(f"La camera {self.room_number} per il periodo {self.date_range} è già prenotata")

    def cancel(self) -> None:
        if self.is_booked:
            self.is_booked = False
        
        else:
            print(f"La prenotazione per la camera {self.room_number} non risulta attiva")

class Guest:
    def __init__(self, guest_id: str, name: str):
        self.guest_id = guest_id
        self.name = name
        self.bookings: list[RoomBooking] = []

    def book_room(self, booking: RoomBooking) -> None:
        if booking.is_booked:
            print(f"La camera {booking.room_number} non è disponibile per il periodo richiesto")
        
        else:
            booking.book()
            self.bookings.append(booking)
            

    def cancel_booking(self, booking: RoomBooking) -> None:
        if booking in self.bookings:
            self.bookings.remove(booking)
            booking.cancel()
        else:
            print(f"La prenotazione per la camera {booking.room_number} non è stata trovata tra quelle del cliente")
    
class Hotel:
    def __init__(self):
        self.bookings: dict[str, RoomBooking] = {}
        self.guests: dict[str, Guest] = {}
    
    def add_booking(self, booking_id: str, room_number: int, date_range: str) -> None:
        if booking_id in self.bookings:
            print(f"La prenotazione con ID {booking_id} esiste già")
        else:
            self.bookings[booking_id] = RoomBooking(booking_id, room_number, date_range)
    
    def register_guest(self, guest_id: str, name: str) -> None:
        if guest_id in self.guests:
            print(f"Il cliente con ID {guest_id} è già registrato")
        else:
            self.guests[guest_id] = Guest(guest_id, name)
    
    def book_room(self, guest_id: str, booking_id: str) -> None:
        if guest_id in self.guests and booking_id in self.bookings:
            guest = self.guests[guest_id]
            booking = self.bookings[booking_id]

            guest.book_room(booking)
        
        else:
            print("Cliente o prenotazione non trovata")
    
    def cancel_room(self, guest_id: str, booking_id: str) -> None:
        if guest_id in self.guests and booking_id in self.bookings:
            guest = self.guests[guest_id]
            booking = self.bookings[booking_id]

            guest.cancel_booking(booking)
        
        else:
            print("Cliente o prenotazione non trovata")
    
    def list_available_rooms(self) -> list[str]:
        return [booking_id for booking_id, booking in self.bookings.items() if not booking.is_booked]
    
    def list_guest_bookings(self, guest_id: str) -> list[str]|str:
        if guest_id in self.guests:
            guest = self.guests[guest_id]
            return [booking.booking_id for booking in guest.bookings]
        
        else:
            return "Errore, cliente non trovato"
