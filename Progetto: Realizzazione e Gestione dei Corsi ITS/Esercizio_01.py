# Esercizio 1
'''
In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e docenti- in gruppi di studio (parte 2), e corsi (parte 3).
 
### Classe Room:
La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats) e un'area (area). 
L'area è calcolata come il doppio dei posti.
- Metodi:
    - get_id(): Restituisce l'ID dell'aula.
    - get_floor(): Restituisce il piano dell'aula.
    - get_seats(): Restituisce il numero di posti dell'aula.
    - get_area(): Restituisce l'area dell'aula.

### Classe Building:
La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address), 
un intervallo di piani (floors), e una lista di aule (rooms).
- Metodi:
    - get_floors(): Restituisce l'intervallo di piani dell'edificio.
    - get_rooms(): Restituisce la lista delle aule nell'edificio.
    - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso 
    nell'intervallo di piani dell'edificio.
    - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.
'''

class Room:

    def __init__(self, id:str, floor:int, seats:int):
        self.id = id
        self.floor = floor
        self.seats = seats

    def get_id(self) -> str:
        return self.id
    
    def get_floor(self) -> int:
        return self.floor
    
    def get_seats(self) -> int:
        return self.seats
    
    def get_area(self) -> int:
        return self.seats * 2


class Building:

    def __init__(self, name:str, address:str, floors:tuple):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = {}
    
    def get_floors(self):
        return self.floors
    
    def get_rooms(self):
        return list(self.rooms.values())
    
    def add_room(self, room: Room):
        if self.floors[0] <= room.get_floor() <= self.floors[1] and room.get_id() not in self.rooms:
            self.rooms[room.get_id()] = room
    
    def area(self):
        return sum(room.get_area() for room in self.rooms.values())

        

# Creazione di stanze
room1 = Room(id="Room1", floor=1, seats=15)
room2 = Room(id="Room2", floor=5, seats=20)
room3 = Room(id="Room3", floor=11, seats=10)  # Questo piano è fuori dal range

# Test classe Room
print("Test classe Room:")
print(f"ID: {room1.get_id()}, Atteso: Room1")
print(f"Piano: {room1.get_floor()}, Atteso: 1")
print(f"Posti: {room1.get_seats()}, Atteso: 15")
print(f"Area: {room1.get_area()}, Atteso: 30")

# Creazione di un edificio
building = Building(name="Test Building", address="123 Test St", floors=(1, 10))

# Test di inizializzazione Building
print("\nTest di inizializzazione Building:")
print(f"Nome: {building.name}, Atteso: Test Building")
print(f"Indirizzo: {building.address}, Atteso: 123 Test St")
print(f"Piani: {building.floors}, Atteso: (1, 10)")
print(f"Stanze iniziali: {building.get_rooms()}, Atteso: []")

# Test aggiunta stanza valida
building.add_room(room1)
print("\nDopo aggiunta Room1:")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test aggiunta stanza su piano non valido
building.add_room(room3)
print("\nDopo tentativo di aggiunta Room3 (piano non valido):")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test aggiunta stanza duplicata
building.add_room(room1)
print("\nDopo tentativo di aggiunta duplicato Room1:")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test calcolo area
building.add_room(room2)
print("\nDopo aggiunta Room2:")
print(f"Area totale: {building.area()}, Atteso: 70")

# Test rappresentazione in stringa Building
print("\nRappresentazione in stringa dell'edificio:")
print(f"Nome Edificio: {building.name}")
print(f"Indirizzo Edificio: {building.address}")
print(f"Piani Edificio: {building.get_floors()}")
print("Stanze nell'edificio:")
for room in building.get_rooms():
    print(f"ID Stanza: {room.get_id()}, Piano: {room.get_floor()}, Posti: {room.get_seats()}, Area: {room.get_area()}")
print(f"Area totale dell'edificio: {building.area()}m2")

# Verifica valori attesi
atteso_stanze = ["Room1", "Room2"]
atteso_area = 70
print(f"\nVerifica finale: Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: {atteso_stanze}")
print(f"Verifica finale: Area totale: {building.area()}, Atteso: {atteso_area}")