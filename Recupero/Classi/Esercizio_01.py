# Esercizio 01

'''
Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di
creare, modificare, e cercare contatti basati sui numeri di telefono. Il sistema dovrà
essere capace di gestire una collezione (dizionario) di contatti e i loro numeri di telefono.

1. Classe ContactManager:
Gestisce tutte le operazioni legate ai contatti.

Attributi:
● contacts: dict[str, list[str]] - Dizionario che ha per chiave il nome del contatto e per
valore una lista di numeri di telefono. I numeri di telefono sono espressi
sottoforma di stringa.

Metodi:
● create_contact(name: str, phone_numbers: list[str]): Crea un nuovo contatto,
aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri
di telefono. Restituisce un nuovo dizionario con il solo contatto appena creato o il
messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già.

● add_phone_number(contact_name: str, phone_number: str): Aggiunge un numero
di telefono al contatto specificato. Restituisce un nuovo dizionario con il solo
contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il
contatto non esiste oppure "Errore: il numero di telefono esiste già." se il numero
di telefono è già presente per il contatto specificato.

● remove_phone_number(contact_name: str, phone_number: str): Rimuove un
numero di telefono dal contatto specificato. Restituisce un nuovo dizionario con il
solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se
il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il
numero di telefono non esiste per il contatto specificato.

● update_phone_number(contact_name: str, old_phone_number: str,
new_phone_number: str): Sostituisce un numero di telefono con un altro nel
contatto specificato. Restituisce un nuovo dizionario con il solo contatto
aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non
esiste oppure "Errore: il numero di telefono non è presente." se il numero di
telefono non esiste per il contatto specificato.

● list_contacts(): Ritorna una lista di tutte le chiavi all'interno del dizionario
contacts.

● list_phone_numbers(contact_name: str): Mostra i numeri di telefono di un
contatto specifico. Restituisce la lista dei numeri di telefono o il messaggio di
errore "Errore: il contatto non esiste." se il contatto non esiste.

● search_contact_by_phone_number(phone_number: str): Trova e restituisce tutti i
contatti che contengono un determinato numero di telefono. Restituisce una lista
di tutte le chiavi all'interno del dizionario contacts che hanno il numero
specificato tra i valori oppure il messaggio di errore "Nessun contatto trovato con
questo numero di telefono." se nessun contatto contiene il numero di telefono.
'''

class ContactManager:

    def __init__(self, contacts: dict[str, list[str]] = None):
        if contacts is None:
            contacts = {}
        self.contacts = contacts
    
    def create_contact(self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:
        if name in self.contacts:
            raise ValueError(f"Errore: il contatto '{name}' esiste già.")
        
        if not isinstance(phone_numbers, list) or not all(isinstance(num, str) for num in phone_numbers):
            raise ValueError("Errore: tutti i numeri di telefono presente nella lista devono essere stringhe")
        
        self.contacts[name] = phone_numbers
        return {name: phone_numbers}
    
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        if self.contacts.get(contact_name) is None:
            raise ValueError(f"Errore: il contatto '{contact_name}' non esiste")
        
        if phone_number in self.contacts[contact_name]:
            raise ValueError(f"Errore: il numero di telefono '{phone_number}' esiste già")
        
        self.contacts[contact_name].append(phone_number)

        return {contact_name: self.contacts[contact_name]}
    
    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:

        if contact_name not in self.contacts:
            raise ValueError(f"Errore: il contatto '{contact_name}' non esiste")
        
        if phone_number not in self.contacts[contact_name]:
            raise ValueError(f"Errore: il numero di telefono '{phone_number}' non è presente")
        
        self.contacts[contact_name].remove(phone_number)

        return {contact_name: self.contacts[contact_name]}
    
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict[str, list[str]]:
        if contact_name not in self.contacts:
            raise ValueError(f"Errore: il contatto '{contact_name}' non esiste")
        
        if old_phone_number not in self.contacts[contact_name]:
            raise ValueError(f"Errore: il numero di telefono '{old_phone_number}' non è presente")
        
        indice = self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][indice] = new_phone_number

        return {contact_name: self.contacts[contact_name]}

    def list_contacts(self) -> list[str]:
        return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name: str) -> list[str]:
        if contact_name not in self.contacts:
            raise ValueError(f"Errore: il contatto '{contact_name}' non esiste")
        
        return self.contacts[contact_name]
    
    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:
        trovare_contatti = []

        for contatto, numero in self.contacts.items():
            if phone_number in numero:
                trovare_contatti.append(contatto)

        # versione con list comprehension
        trovare_contatti = [contatto for contatto, numero in self.contacts.items() if phone_number in numero] 
            
        if not trovare_contatti:
            raise ValueError(f"Errore: Nessun contatto trovato con il numero di telefono '{phone_number}'")
        
        return trovare_contatti

if __name__ == "__main__":

    # creo un'istanza del gestore contatti
    manager = ContactManager()

    # creo un nuovo contatto
    try:
        print("- Creazione di contatto -\n")
        manager.create_contact("Rodolfo Ancud", ["123456789", "159753483"])
        manager.create_contact("Buhaiola Spaziale", ["147852369"])
        manager.create_contact("Buhaiolìn Bombìn", ["697184532", "787945612"])
    
    except ValueError as e:
        print(e)
    
    print(manager.contacts)

    # aggiungo numero di telefono a un contatto
    try:
        print("\n- Aggiungere numero di telefono alla lista:\n")
        manager.add_phone_number("Rodolfo Ancud", "753468215")
        manager.add_phone_number("Buhaiola Espazial", "456789123")
    
    except ValueError as e:
        print(e)
    print(manager.contacts)

    # rimuovo numero di telefono a un contatto
    try:
        print("\n- Rimozione di numero di telefono:\n")
        # manager.remove_phone_number("Rodolfo Ancud", "123698745")
        manager.remove_phone_number("Buhaiolìn Bombìn", "787945612")
    
    except ValueError as e:
        print(e)
    print(manager.contacts)

    # aggiornare il numero di telefono
    try:
        print("\n- Numeri di telefono aggionarti:\n")
        manager.update_phone_number("Buhaiola Spaziale", "147852369", "987654753")

    except ValueError as e:
        print(e)
    print(manager.contacts)

    # lista dei contatti
    
    print("\n- Lista dei contatti:\n")
    print(manager.list_contacts())

    # lista dei numeri di telefono dei contatti
    try:
        print("\n- Lista dei numeri di telefono:\n")
        print(manager.list_phone_numbers("Rodolfo Ancud"))
        print(manager.list_phone_numbers("Buhaiola Spaziale"))
        print(manager.list_phone_numbers("Buhaiolìn Bombìn"))
    
    except ValueError as e:
        print(e)
    
    # trovare un contatto tramite il numero di telefono
    try:
        print("\nRicerca contatto per numero:\n")
        print(manager.search_contact_by_phone_number("147852369"))
        print(manager.search_contact_by_phone_number("753468215"))
    
    except ValueError as e:
        print(e)
    
    # verficare si un contatto esiste
    try:
        print("\nVerifica contatto esistente:\n")
        manager.create_contact("Buhaiolìn Bombìn", ["787945612"])
        manager.create_contact("Topolino Gnugnoino", ["654357951", "123147369"])
    except ValueError as e:
        print(e)
    print(manager.contacts)

    
