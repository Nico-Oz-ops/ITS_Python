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