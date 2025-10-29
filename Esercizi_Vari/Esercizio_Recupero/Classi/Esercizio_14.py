'''
Esercizio: Gestore di Contatti (ContactManager)

Scrivi una classe chiamata ContactManager che gestisca una rubrica di contatti.
Ogni contatto è salvato in un dizionario principale, dove la chiave è l’ID del 
contatto e il valore è un sotto-dizionario con i suoi dati.

Struttura dati:
self.contatti = {
    "c001": {
        "nome": "Mario Rossi",
        "telefono": "3331234567",
        "email": "mario.rossi@email.it"
    },
    "c002": {
        "nome": "Lucia Bianchi",
        "telefono": "3459876543",
        "email": "lucia.bianchi@email.it"
    }
}

Metodi richiesti:

* add_contact(contact_id: str, nome: str, telefono: str, email: str) -> dict | str
Aggiunge un nuovo contatto.

    * Se l’ID esiste già, restituisce "Errore, contatto già esistente."
    * Se è nuovo, aggiunge il contatto e restituisce il dizionario del contatto creato.

Esempio:

manager.add_contact("c001", "Mario Rossi", "3331234567", "mario@email.it")


* update_phone(contact_id: str, nuovo_telefono: str) -> dict | str
Aggiorna il numero di telefono di un contatto esistente.

    * Se il contatto non esiste, restituisce "Errore, contatto non trovato."
    * Se esiste, aggiorna e restituisce il contatto modificato.

* update_email(contact_id: str, nuova_email: str) -> dict | str
Aggiorna l’email del contatto.

    * Se non trovato, restituisce "Errore, contatto non trovato."
    * Se trovato, restituisce il contatto aggiornato.

* remove_contact(contact_id: str) -> dict | str
Rimuove un contatto e restituisce i suoi dati.

    * Se non trovato, restituisce "Errore, contatto non trovato."

* get_contact(contact_id: str) -> dict | str
Restituisce i dati del contatto corrispondente all’ID.

    * Se non trovato, restituisce "Errore, contatto non trovato."

* list_contacts() -> list[str]
Restituisce la lista degli ID dei contatti salvati.

* find_by_name(nome: str) -> dict | str
Cerca tutti i contatti che corrispondono al nome indicato (ricerca case-insensitive).

    * Se trova corrispondenze, restituisce un dizionario con i risultati.
    * Se non trova nulla, restituisce "Nessun contatto trovato con questo nome."
'''

class ContactManager:
    def __init__(self):
        self.contatti: dict[str, dict] = {}
    
    def add_contact(self, contact_id: str, nome: str, telefono: str, email: str) -> dict|str:
        if contact_id in self.contatti:
            return "Errore, contatto già esistente"
        self.contatti[contact_id] = {"nome": nome, "telefono": telefono, "email": email}

        return {contact_id: self.contatti[contact_id]}

    def update_phone(self, contact_id: str, nuovo_telefono: str) -> dict|str:
        if contact_id not in self.contatti:
            return "Errore, contatto non trovato"
        self.contatti[contact_id]["telefono"] = nuovo_telefono

        return {contact_id: self.contatti[contact_id]}

    def update_email(self, contact_id: str, nuova_email: str) -> dict|str:
        if contact_id not in self.contatti:
            return "Errore, contatto non trovato"
        self.contatti[contact_id]["email"] = nuova_email

        return {contact_id: self.contatti[contact_id]}
    
    def remove_contact(self, contact_id: str) -> dict|str:
        if contact_id not in self.contatti:
            return "Errore, contatto non trovato"
        contatto_rimosso = self.contatti.pop(contact_id)

        return {contact_id: contatto_rimosso}
    
    def get_contact(self, contact_id: str) -> dict|str:
        if contact_id not in self.contatti:
            return "Errore, contatto non trovato"
        return {contact_id: self.contatti[contact_id]}

    def list_contacts(self) -> list[str]:
        return list(self.contatti.keys())

    def find_by_name(self, nome: str) -> dict|str:
        risultati = {}

        for contact_id, info in self.contatti.items():
            if info["nome"].lower() == nome.lower():
                risultati[contact_id] = info
        
        if risultati:
            return risultati
        else:
            return "Nessun contatto trovato con questo nome"


manager = ContactManager()

manager.add_contact("c001", "Mario Rossi", "3331234567", "mario@email.it")
manager.add_contact("c002", "Lucia Bianchi", "3459876543", "lucia@email.it")
manager.add_contact("c003", "mario verdi", "3209999999", "m.verdi@email.it")

print(manager.find_by_name("mario"))