'''
Esercizio: Classe DeliveryManager

Progetta una classe DeliveryManager per gestire un insieme di spedizioni.

A. Attributi:

* deliveries: dict[str, dict]
    * Un dizionario in cui:
        * la chiave è un delivery_id (str)
        * il valore è un altro dizionario con queste chiavi e valori:
            * "destinazione" (str): la città o indirizzo di destinazione
            * "inviato" (bool): True se la spedizione è già stata inviata, altrimenti False

B. Metodi:

* add_delivery(delivery_id: str, destinazione: str) -> dict | str
Se delivery_id esiste già, restituisci:
"Errore: spedizione già registrata."
Altrimenti aggiungi la nuova spedizione con "inviato": False e restituisci il dizionario della spedizione.

* mark_as_sent(delivery_id: str) -> dict | str
Se delivery_id non esiste, restituisci:
"Errore: spedizione non trovata."
Altrimenti imposta "inviato" a True e restituisci il dizionario aggiornato.

* update_destination(delivery_id: str, nuova_destinazione: str) -> dict | str
Se delivery_id non esiste, restituisci:
"Errore: spedizione non trovata."
Altrimenti aggiorna la destinazione e restituisci il dizionario aggiornato.

* cancel_delivery(delivery_id: str) -> dict | str
Se delivery_id non esiste, restituisci:
"Errore: spedizione non trovata."
Altrimenti imposta "inviato" a False e restituisci il dizionario aggiornato.

* remove_delivery(delivery_id: str) -> dict | str
Se delivery_id non esiste, restituisci:
"Errore: spedizione non trovata."
Altrimenti rimuovi la spedizione e restituisci il dizionario rimosso.

* list_deliveries() -> list[str]
Restituisce la lista di tutti i delivery_id.

* get_delivery(delivery_id: str) -> dict | str
Se esiste, restituisci il dizionario della spedizione.
Altrimenti: "Errore: spedizione non trovata."
'''

class DeliveryManager:
    def __init__(self):
        self.deliveries: dict[str, dict] = {}
    
    def add_delivery(self, delivery_id: str, destinazione: str) -> dict|str:
        if delivery_id in self.deliveries:
            return "Errore: spedizione già registrata."
        self.deliveries[delivery_id] = {"destinazione": destinazione, "inviato": False}

        return {delivery_id: self.deliveries[delivery_id]}

    def mark_as_sent(self, delivery_id: str) -> dict|str:
        if delivery_id not in self.deliveries:
            return "Errore: spedizione non trovata."
        self.deliveries[delivery_id]["inviato"] = True

        return {delivery_id: self.deliveries[delivery_id]}
    
    def update_destination(self, delivery_id: str, nuova_destinazione: str) -> dict|str:
        if delivery_id not in self.deliveries:
            return "Errore: spedizione non trovata."
        self.deliveries[delivery_id]["destinazione"] = nuova_destinazione

        return {delivery_id: self.deliveries[delivery_id]}

    def cancel_delivery(self, delivery_id: str) -> dict|str:
        if delivery_id not in self.deliveries:
            return "Errore: spedizione non trovata."
        self.deliveries[delivery_id]["inviato"] = False

        return {delivery_id: self.deliveries[delivery_id]}
    
    def remove_delivery(self, delivery_id: str) -> dict|str:
        if delivery_id not in self.deliveries:
            return "Errore: spedizione non trovata."
        spedizione_rimossa = self.deliveries.pop(delivery_id)

        return {delivery_id: spedizione_rimossa}
    
    def list_deliveries(self) -> list[str]:
        return list(self.deliveries.keys())
    
    def get_delivery(self, delivery_id: str) -> dict|str:
        if delivery_id not in self.deliveries:
            return "Errore: spedizione non trovata."
        
        return {delivery_id: self.deliveries[delivery_id]}


d = DeliveryManager()

print(d.add_delivery("D001", "Milano"))
print(d.add_delivery("D002", "Roma"))
print(d.mark_as_sent("D001"))
print(d.update_destination("D002", "Napoli"))
print(d.cancel_delivery("D001"))
print(d.get_delivery("D001"))
print(d.remove_delivery("D002"))
print(d.list_deliveries())
        