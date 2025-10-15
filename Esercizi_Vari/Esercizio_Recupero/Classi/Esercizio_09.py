'''
Esercizio: Classe ProjectManager

Progetta una classe ProjectManager per gestire un insieme di progetti aziendali.

A. Attributi:

* projects: dict[str, dict]

Un dizionario in cui:

    * la chiave è un project_id (str)
    * il valore è un altro dizionario con queste chiavi e valori:

        * "nome" (str): nome del progetto
        * "completato" (bool): True se il progetto è stato completato, altrimenti False
        * "budget" (float): budget assegnato al progetto

B. Metodi:

    * add_project(project_id: str, nome: str, budget: float) -> dict | str
    Se project_id esiste già, restituisci:
    "Errore: progetto già registrato."
    Altrimenti aggiungi il nuovo progetto con "completato": False e restituisci il dizionario del progetto.

    * mark_as_completed(project_id: str) -> dict | str
    Se project_id non esiste, restituisci:
    "Errore: progetto non trovato."
    Altrimenti imposta "completato" a True e restituisci il dizionario aggiornato.

    * update_name(project_id: str, nuovo_nome: str) -> dict | str
    Se project_id non esiste, restituisci:
    "Errore: progetto non trovato."
    Altrimenti aggiorna il nome del progetto e restituisci il dizionario aggiornato.

    * update_budget(project_id: str, nuovo_budget: float) -> dict | str
    Se project_id non esiste, restituisci:
    "Errore: progetto non trovato."
    Altrimenti aggiorna il budget e restituisci il dizionario aggiornato.

    * remove_project(project_id: str) -> dict | str
    Se project_id non esiste, restituisci:
    "Errore: progetto non trovato."
    Altrimenti rimuovi il progetto e restituisci il dizionario rimosso.

    * list_projects() -> list[str]
    Restituisce la lista di tutti i project_id.

    * get_project(project_id: str) -> dict | str
    Se esiste, restituisci il dizionario del progetto.
    Altrimenti: "Errore: progetto non trovato."
'''