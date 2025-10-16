'''
Esercizio: Classe TaskManager

Progetta una classe TaskManager per gestire un insieme di attività lavorative.

A. Attributi:

* tasks: dict[str, dict]

Un dizionario in cui:

    * la chiave è un task_id (str)
    * il valore è un altro dizionario con queste chiavi e valori:

        * "descrizione" (str): descrizione del task
        * "completato" (bool): True se il task è stato completato, altrimenti False
        * "priorità" (int): livello di priorità del task (1-5)

B. Metodi:

    * add_task(task_id: str, descrizione: str, priorità: int) -> dict | str
    Se task_id esiste già, restituisci:
    "Errore: task già registrato."
    Altrimenti aggiungi il nuovo task con "completato": False e restituisci il dizionario del task.

    * mark_as_done(task_id: str) -> dict | str
    Se task_id non esiste, restituisci:
    "Errore: task non trovato."
    Altrimenti imposta "completato" a True e restituisci il dizionario aggiornato.

    * update_description(task_id: str, nuova_descrizione: str) -> dict | str
    Se task_id non esiste, restituisci:
    "Errore: task non trovato."
    Altrimenti aggiorna la descrizione e restituisci il dizionario aggiornato.

    * change_priority(task_id: str, nuova_priorità: int) -> dict | str
    Se task_id non esiste, restituisci:
    "Errore: task non trovato."
    Altrimenti aggiorna la priorità e restituisci il dizionario aggiornato.

    * remove_task(task_id: str) -> dict | str
    Se task_id non esiste, restituisci:
    "Errore: task non trovato."
    Altrimenti rimuovi il task e restituisci il dizionario rimosso.

    * list_tasks() -> list[str]
    Restituisce la lista di tutti i task_id.

    * get_task(task_id: str) -> dict | str
    Se esiste, restituisci il dizionario del task.
    Altrimenti: "Errore: task non trovato."
'''

class TaskManager:
    def __init__(self):
        self.tasks: dict[str, dict] = {}
    
    def add_task(self, task_id: str, descrizione: str, priorita: int) -> dict|str:
        if task_id in self.tasks:
            return "Errore: task già registrato"
        self.tasks[task_id] = {"descrizione": descrizione, "completato": False, "priorità": priorita}

        return {task_id: self.tasks[task_id]}
    
    def mark_as_done(self, task_id:str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        self.tasks[task_id]["completato"] = True

        return {task_id: self.tasks[task_id]}
    
    def update_description(self, task_id: str, nuova_descrizione: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        self.tasks[task_id]["descrizione"] = nuova_descrizione

        return {task_id: self.tasks[task_id]}
    
    def change_priority(self, task_id: str, nuova_priorita: int) -> dict|str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        self.tasks[task_id]["priorità"] = nuova_priorita

        return {task_id: self.tasks[task_id]}
    
    def remove_task(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        task_rimosso = self.tasks.pop(task_id)

        return {task_id: task_rimosso}
    
    def list_tasks(self) -> list[str]:
        return list(self.tasks.keys())
    
    def get_task(self, task_id: str) -> dict|str:
        if task_id not in self.tasks:
            return "Errore: task non trovato"
        return {task_id: self.tasks[task_id]}

