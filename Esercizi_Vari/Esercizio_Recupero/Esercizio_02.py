'''
Scrivi una classe chiamata CalendarManager che permetta di gestire una lista di eventi. 
Ogni evento ha un ID, una descrizione, una data, e uno stato confermato (booleano).
 
Specifiche della classe:
class CalendarManager:
    def __init__(self, eventi: dict[str, dict] = None):
    es. 
    {
    "event1": {
        "descrizione": "Concerto rock",
        "data": "2025-10-01",
        "confermato": False
    }
}
 
Metodi richiesti:
 
- create_event(self, event_id: str, descrizione: str, data: str) -> dict | str
Crea un nuovo evento con ID, descrizione e data. Lo stato "confermato" sarà inizialmente False.
Se l’evento esiste già, solleva un ValueError.
 
- confirm_event(self, event_id: str) -> dict | str
Imposta lo stato "confermato" a True.
Se l’evento non esiste, solleva un ValueError.
 
- update_event(self, event_id: str, nuova_descrizione: str, nuova_data: str) -> dict | str
Aggiorna descrizione e data dell’evento.
Se l’evento non esiste, solleva un ValueError.
 
- remove_event(self, event_id: str) -> dict | str
Rimuove un evento dalla lista.
Se l’evento non esiste, solleva un ValueError.
 
- list_events(self) -> list[str]
Restituisce una lista di ID di tutti gli eventi.
 
- get_event(self, event_id: str) -> dict | str
Restituisce i dettagli di un evento dato il suo ID.
Se l’evento non esiste, restituisce "Evento non trovato".
'''

class CalendarManager:
    def __init__(self, eventi: dict[str, dict] = None):
        self.eventi = eventi if eventi is not None else {}
    
    def create_event(self, event_id: str, descrizione: str, data: str) -> dict|str:
        if event_id in self.eventi:
            raise ValueError ("Errore: l'evento esiste già")
        self.eventi[event_id] = {"descrizione": descrizione, "data": data, "confermato": False}
        return {event_id: self.eventi[event_id]}
    
    def confirm_event(self, event_id: str):
        if event_id not in self.eventi:
            raise ValueError("Errore: l'evento non esiste")
        self.eventi[event_id]["confermato"] = True
        return {event_id: self.eventi[event_id]}
    
    def update_event(self, event_id: str, nuova_descrizione: str, nuova_data: str):
        if event_id not in self.eventi:
            raise ValueError("Errore: l'evento non esiste")
        self.eventi[event_id]["descrizione"] = nuova_descrizione
        self.eventi[event_id]["data"] = nuova_data
        return {event_id: self.eventi[event_id]}
    
    def remove_event(self, event_id: str):
        if event_id not in self.eventi:
            raise ValueError("Errore: l'evento non esiste")
        return {event_id: self.eventi.pop(event_id)}
    
    def list_events(self) -> list[str]:
        return list(self.eventi.keys())
    
    def get_event(self, event_id: str):
        if event_id not in self.eventi:
            return "Errore: l'evento non esiste"
        return {event_id: self.eventi[event_id]}
        


        
        