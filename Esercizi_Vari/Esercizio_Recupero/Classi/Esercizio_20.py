'''
Esercizio: Gestore di Palestra (GymManager)

Scrivi una classe chiamata GymManager che gestisca i membri, le attrezzature e le iscrizioni della palestra.

-----------------------------------------------------------
Struttura dati:
-----------------------------------------------------------

self.attrezzature: dict[str, dict]
Contiene le attrezzature disponibili nella palestra.
La chiave è l'ID dell'attrezzatura e il valore è un dizionario con:

    "nome" (str): nome dell'attrezzatura.
    "quantita" (int): numero totale di attrezzature disponibili.
    "disponibile" (int): numero di attrezzature disponibili per l’uso.

self.membri: dict[str, dict]
Contiene i membri iscritti alla palestra.
La chiave è l'ID del membro e il valore è un dizionario con:

    "nome" (str): nome del membro.
    "email" (str): email del membro.
    "iscrizione" (str): data di iscrizione (formato "YYYY-MM-DD").
    "abbonamento_attivo" (bool): True se l’abbonamento è attivo, False se scaduto.

-----------------------------------------------------------
Metodi richiesti:
-----------------------------------------------------------

* add_member(member_id: str, nome: str, email: str, iscrizione: str, abbonamento_attivo: bool = True) -> dict | str
Aggiunge un nuovo membro alla palestra.

    * Se l’ID esiste già, restituisce "Errore, membro già registrato".
    * Altrimenti aggiunge il membro con i dati forniti (abbonamento_attivo di default True)
      e restituisce il dizionario del membro aggiunto.


* remove_member(member_id: str) -> dict | str
Rimuove un membro dalla palestra.

    * Se l’ID non esiste, restituisce "Errore, membro non trovato".
    * Se trovato, rimuove il membro e restituisce i suoi dati.


* update_membership(member_id: str, abbonamento_attivo: bool) -> dict | str
Aggiorna lo stato dell’abbonamento di un membro.

    * Se l’ID non esiste, restituisce "Errore, membro non trovato".
    * Se trovato, aggiorna il campo "abbonamento_attivo" e restituisce i dati aggiornati.


* add_equipment(equipment_id: str, nome: str, quantita: int) -> dict | str
Aggiunge una nuova attrezzatura alla palestra.

    * Se l’ID esiste già, restituisce "Errore, attrezzatura già presente".
    * Altrimenti aggiunge l’attrezzatura con "disponibile" uguale a "quantita"
      e restituisce il dizionario dell’attrezzatura aggiunta.


* remove_equipment(equipment_id: str) -> dict | str
Rimuove un’attrezzatura dalla palestra.

    * Se l’ID non esiste, restituisce "Errore, attrezzatura non trovata".
    * Se trovata, rimuove e restituisce i suoi dati.


* update_equipment(equipment_id: str, nuova_quantita: int) -> dict | str
Aggiorna la quantità di una determinata attrezzatura.

    * Se l’ID non esiste, restituisce "Errore, attrezzatura non trovata".
    * Se trovato, aggiorna sia "quantita" che "disponibile" (se coerente) e restituisce i dati aggiornati.


* list_members() -> list[str]
Restituisce la lista di tutti gli ID dei membri registrati nella palestra.


* list_equipment() -> list[str]
Restituisce la lista di tutti gli ID delle attrezzature disponibili nella palestra.


* find_member_by_name(nome: str) -> dict | str
Cerca i membri che corrispondono (anche parzialmente, case-insensitive) al nome indicato.

    * Se trova corrispondenze, restituisce un dizionario {id_membro: dati_membro}.
    * Se non trova nulla, restituisce "Nessun membro trovato con questo nome."


* find_equipment_by_name(nome: str) -> dict | str
Cerca le attrezzature che corrispondono (anche parzialmente, case-insensitive) al nome indicato.

    * Se trova corrispondenze, restituisce un dizionario {id_attrezzatura: dati_attrezzatura}.
    * Se non trova nulla, restituisce "Nessuna attrezzatura trovata con questo nome."
'''

