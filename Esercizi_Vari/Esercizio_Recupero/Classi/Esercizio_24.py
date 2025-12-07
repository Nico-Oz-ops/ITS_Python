'''
Gestione Parcheggio

Progetta una classe ParkingLot per la gestione dei posti auto (spazi) in un parcheggio. Ogni posto è identificato da un numero intero.

---

Classe ParkingLot

Attributi

• spaces: dict[int, dict]: Dizionario che mappa il numero del posto (intero) ai dettagli del posto. I dettagli sono un dizionario con: "occupato": bool e "targa": str | None.

Metodi

• add_space(numero: int) -> bool
Controlla se numero (il posto) esiste già in spaces. Se sì, restituisce False. Altrimenti, aggiunge il nuovo posto (impostandolo come occupato=False e targa=None) e restituisce True.

• remove_space(numero: int) -> dict | str
Cerca numero in spaces. Se non esiste, restituisce "Errore: posto inesistente.". Se esiste ma è occupato=True, restituisce "Errore: posto occupato.". Se esiste ed è occupato=False, lo rimuove da spaces e restituisce un dizionario contenente solo i dettagli del posto rimosso.

• park_car(numero: int, targa: str) -> str
Cerca numero in spaces. Se non esiste, restituisce "Errore: posto inesistente.". Se esiste ma è occupato=True, restituisce "Errore: posto già occupato.". Se esiste ed è libero, imposta occupato=True, salva la targa e restituisce "Auto parcheggiata con successo.".

• leave_space(numero: int) -> str
Cerca numero in spaces. Se non esiste, restituisce "Errore: posto inesistente.". Se esiste ma è occupato=False, restituisce "Errore: posto già libero.". Se esiste ed è occupato, imposta occupato=False e targa=None, e restituisce "Posto liberato con successo.".

• list_free_spaces() -> list[int]
Scorre tutti i posti in spaces e restituisce una lista contenente i numeri (le chiavi) di solo quei posti che hanno occupato=False.

• get_space_info(numero: int) -> dict | str
Cerca numero in spaces. Se non esiste, restituisce "Errore: posto inesistente.". Altrimenti, restituisce il dizionario interno contenente i dettagli di quel posto (stato di occupazione e targa). (es. {"occupato" : True, "targa" : "AB123CD"}).

---

[TRACCIA ESERCIZIO 2 - SISTEMA E-COMMERCE]

Sistema E-commerce

Progetta e implementa un semplice sistema e-commerce in Python, organizzato attorno a tre classi principali: Product, ShoppingCart e Shop. Ogni classe deve essere chiara nel proprio scopo e ogni funzione deve essere ben documentata con responsabilità ben definite.

---

Classe Product

Rappresenta un singolo prodotto venduto nel negozio online. Ogni prodotto ha informazioni uniche e uno stock che ne regola la disponibilità.

Attributi

· product_id: str -- Identificatore unico del prodotto nello shop (esempio: "SKU1234"). Serve per distinguere ogni articolo.
· name: str -- Nome del prodotto (esempio: "Mouse Wireless Logitech").
· price: float -- Prezzo unitario del prodotto in euro (ad esempio 29.90).
· stock: int -- Quantità attualmente disponibile a magazzino per il prodotto.

Metodi

· update_stock(quantity: int) -> None -- Aggiorna la quantità disponibile del prodotto. Se il parametro è positivo la quantità viene aumentata, se negativo viene diminuita. Non restituisce nulla.
· is_available(quantity: int) -> bool -- Controlla se il prodotto ha almeno la quantità richiesta disponibile (utile per le vendite). Ritorna True se lo stock è sufficiente, False altrimenti.

---

Classe ShoppingCart

Questa classe simula il carrello di un utente, che può contenere più prodotti con relative quantità. Opera come un contenitore temporaneo delle scelte d'acquisto prima del pagamento.

Attributi

· items: dict[str, int] -- Dizionario che associa ogni product_id alla quantità richiesta da acquistare da parte dell'utente. Esempio: { 'SKU1234': 2, 'SKU5678': 1}.

Metodi

· add_item(product: Product, quantity: int) -> str -- Tenta di aggiungere il prodotto al carrello nella quantità richiesta. Se la quantità disponibile non è sufficiente, restituisce un messaggio di errore. Se l'aggiunta va a buon fine, aggiorna lo stock del prodotto (diminuisce di quantity) e ritorna un messaggio di conferma.
· remove_item(product_id: str) -> str -- Rimuove dal carrello il prodotto corrispondente al product_id. Se il prodotto era presente, lo elimina e restituisce conferma; se non era presente, restituisce un messaggio di errore.
· get_total(products: dict[str, Product]) -> float -- Calcola e ritorna la somma totale degli articoli nel carrello, moltiplicando il prezzo unitario per la quantità di ogni prodotto. Ha bisogno del dizionario dei prodotti per accedere ai prezzi.
· clear() -> None -- Svuota tutto il carrello, rimuovendo tutti i prodotti e le relative quantità.

---

Classe Shop

Gestisce l'inventario dei prodotti e tutti i carrelli attivi (potrebbero corrispondere a diversi utenti o sessioni). Offre metodi per la gestione dei prodotti, la creazione di carrelli e la conclusione dell'acquisto (checkout).

Attributi

· products: dict[str, Product] → Mappa ogni product_id a un oggetto Product rappresentando l'intero inventario del negozio.
· carts: dict[str, ShoppingCart] → Mappa ogni carrello (identificato da un cart_id, es: "cart123") all'oggetto ShoppingCart corrispondente. Così si gestiscono più clienti contemporaneamente.

Metodi

· add_product(product: Product) → str → Aggiunge un nuovo prodotto al negozio. Se il product_id è già presente, non aggiunge il prodotto e restituisce un messaggio di errore; altrimenti, aggiunge il nuovo prodotto e ritorna una stringa di conferma.
· remove_product(product_id: str) → str → Rimuove il prodotto col dato product_id dall'inventario. Restituisce conferma se l'operazione ha successo o un errore se il prodotto non esiste.
· create_cart() → str → Crea un nuovo carrello della spesa, genera un nuovo cart_id (puoi usare ad esempio uuid), lo inserisce nella mappa carts e ritorna il suo id.
· checkout(cart_id: str) → float | str → Conclude l'acquisto per il carrello identificato da cart_id. Se tutti i prodotti nel carrello sono effettivamente disponibili nell'inventario, calcola il totale e svuota il carrello.

---

Note Bene

· Ogni metodo dovrebbe controllare con precisione la validità dell'operazione richiesta e fornire messaggi chiari in caso di errore.
· Si assuma che ogni cart_id e product_id sia univoco sul sistema.
· L'esercizio valuterà la correttezza dell'organizzazione delle classi e delle responsabilità di ogni metodo.
'''


class ParkingLot:
    """Gestisce i posti auto in un parcheggio"""
    
    def __init__(self):
        self.spaces = {} # dict[int, dict] - numero posto -> dettagli
    
    def add_space(self, numero: int) -> bool:
        """Aggiunge un nuovo posto al parcheggio"""
        if numero in self.spaces:
            return False
        else:
            self.spaces[numero] = {"occupato": False, "targa": None}
            return True
    
    def remove_space(self, numero: int) -> dict | str:
        """Rimuove un posto dal parcheggio"""
        if numero not in self.spaces:
            return "Errore: posto inesistente."
        
        if self.spaces[numero]["occupato"]:
            return "Errore: posto occupato."
        
        # Usando pop() per rimuovere e restituire i dettagli in una sola operazione
        return self.spaces.pop(numero)
    
    def park_car(self, numero: int, targa: str) -> str:
        """Parcheggia un'auto in un posto"""
        if numero not in self.spaces:
            return "Errore: posto inesistente."
        
        if self.spaces[numero]["occupato"]:
            return "Errore: posto già occupato."
        
        self.spaces[numero]["occupato"] = True
        self.spaces[numero]["targa"] = targa
        return "Auto parcheggiata con successo."
    
    def leave_space(self, numero: int) -> str:
        """Libera un posto occupato"""
        if numero not in self.spaces:
            return "Errore: posto inesistente."
        
        if not self.spaces[numero]["occupato"]:
            return "Errore: posto già libero."
        
        self.spaces[numero]["occupato"] = False
        self.spaces[numero]["targa"] = None
        return "Posto liberato con successo."
    
    def list_free_spaces(self) -> list[int]:
        """Restituisce la lista dei posti liberi"""
        return [numero for numero, dettagli in self.spaces.items() 
                if not dettagli["occupato"]]
    
    def get_space_info(self, numero: int) -> dict | str:
        """Restituisce i dettagli di un posto specifico"""
        if numero not in self.spaces:
            return "Errore: posto inesistente."
        
        return self.spaces[numero]


# ESEMPIO DI UTILIZZO
if __name__ == "__main__":
    parcheggio = ParkingLot()
    
    # Aggiungi posti
    print(parcheggio.add_space(1)) # True
    print(parcheggio.add_space(2)) # True
    print(parcheggio.add_space(3)) # True
    print(parcheggio.add_space(1)) # False (già esistente)
    
    # Parcheggia auto
    print(parcheggio.park_car(1, "AB123CD")) # Auto parcheggiata con successo
    print(parcheggio.park_car(2, "EF456GH")) # Auto parcheggiata con successo
    print(parcheggio.park_car(1, "IJ789KL")) # Errore: posto già occupato
    print(parcheggio.park_car(4, "MN012OP")) # Errore: posto inesistente
    
    # Lista posti liberi
    print(parcheggio.list_free_spaces()) # [3]
    
    # Info posto
    print(parcheggio.get_space_info(1)) # {'occupato': True, 'targa': 'AB123CD'}
    print(parcheggio.get_space_info(4)) # Errore: posto inesistente
    
    # Libera posto
    print(parcheggio.leave_space(2)) # Posto liberato con successo
    print(parcheggio.leave_space(2)) # Errore: posto già libero
    print(parcheggio.leave_space(4)) # Errore: posto inesistente
    
    # Rimuovi posto
    print(parcheggio.remove_space(3)) # {'occupato': False, 'targa': None}
    print(parcheggio.remove_space(1)) # Errore: posto occupato
    print(parcheggio.remove_space(4)) # Errore: posto inesistente
    
    # Stato finale
    print("Posti rimanenti:", list(parcheggio.spaces.keys())) # [1, 2]