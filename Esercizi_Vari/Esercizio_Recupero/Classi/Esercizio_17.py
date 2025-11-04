'''
Esercizio: Gestore di Magazzino (InventoryManager)

Scrivi una classe chiamata InventoryManager che gestisca un inventario di prodotti.
Ogni prodotto è salvato in un dizionario principale, dove la chiave è l’ID del 
prodotto e il valore è un sotto-dizionario con i suoi dettagli.

Struttura dati:
self.prodotti = {
    "p001": {
        "nome": "Laptop",
        "quantità": 10,
        "prezzo": 899.99
    },
    "p002": {
        "nome": "Mouse",
        "quantità": 50,
        "prezzo": 19.99
    }
}

Metodi richiesti:

* add_product(product_id: str, nome: str, quantità: int, prezzo: float) -> dict | str
Aggiunge un nuovo prodotto.

    * Se l’ID esiste già, restituisce "Errore, prodotto già esistente."
    * Se è nuovo, aggiunge il prodotto e restituisce il dizionario del prodotto creato.

Esempio:

manager.add_product("p001", "Laptop", 10, 899.99)


* update_quantity(product_id: str, nuova_quantità: int) -> dict | str
Aggiorna la quantità disponibile di un prodotto.

    * Se il prodotto non esiste, restituisce "Errore, prodotto non trovato."
    * Se esiste, aggiorna e restituisce il prodotto modificato.

* update_price(product_id: str, nuovo_prezzo: float) -> dict | str
Aggiorna il prezzo di un prodotto.

    * Se non trovato, restituisce "Errore, prodotto non trovato."
    * Se trovato, restituisce il prodotto aggiornato.

* remove_product(product_id: str) -> dict | str
Rimuove un prodotto e restituisce i suoi dati.

    * Se non trovato, restituisce "Errore, prodotto non trovato."

* get_product(product_id: str) -> dict | str
Restituisce i dati del prodotto corrispondente all’ID.

    * Se non trovato, restituisce "Errore, prodotto non trovato."

* list_products() -> list[str]
Restituisce la lista degli ID dei prodotti salvati.

* find_by_name(nome: str) -> dict | str
Cerca tutti i prodotti che corrispondono al nome indicato (ricerca case-insensitive).

    * Se trova corrispondenze, restituisce un dizionario con i risultati.
    * Se non trova nulla, restituisce "Nessun prodotto trovato con questo nome."
'''
class InventoryManager:
    def __init__(self):
        self.prodotti: dict[str, dict] = {}
    
    def add_product(self, product_id: str, nome: str, quantita: int, prezzo: float) -> dict|str:
        if product_id in self.prodotti:
            return "Errore, prodotto già esistente"
        self.prodotti[product_id] = {"nome": nome, "quantità": quantita, "prezzo": prezzo}

        return {product_id: self.prodotti[product_id]}

    def update_quantity(self, product_id: str, nuova_quantita: int) -> dict|str:
        if product_id not in self.prodotti:
            return "Errore, prodotto non trovato"
        self.prodotti[product_id]["quantità"] = nuova_quantita

        return {product_id: self.prodotti[product_id]}
    
    def update_price(self, product_id: str, nuovo_prezzo: float) -> dict|str:
        if product_id not in self.prodotti:
            return "Errore, prodotto non trovato"
        self.prodotti[product_id]["prezzo"] = nuovo_prezzo

        return {product_id: self.prodotti[product_id]}
    
    def remove_product(self, product_id: str) -> dict|str:
        if product_id not in self.prodotti:
            return "Errore, prodotto non trovato"
        prodotto_rimosso = self.prodotti.pop(product_id)

        return {product_id: prodotto_rimosso}

    def get_product(self, product_id: str) -> dict|str:
        if product_id not in self.prodotti:
            return "Errore, prodotto non trovato"
        
        return {product_id: self.prodotti[product_id]}
    
    def list_products(self) -> list[str]:
        return list(self.prodotti.keys())
    
    def find_by_name(self, nome: str) -> dict|str:
        risultati = {}

        for product_id, info_product in self.prodotti.items():
            if info_product["nome"].lower() == nome.lower():
                risultati[product_id] = info_product
        
        if risultati:
            return risultati
        else:
            return "Nessun prodotto trovato con questo nome"


    

