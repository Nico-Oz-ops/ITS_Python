'''
Esercizio: GestoreBiblioteca

Crea una classe per gestire i libri di una piccola biblioteca.

Classe GestoreBiblioteca

A. Attributi:
* libri: dict[str, dict]
Ogni chiave è il codice del libro, e il valore è un dizionario con:
{
"titolo": str,
"autore": str,
"anno_pubblicazione": int,
"disponibile": bool
}

B. Metodi:

* aggiungi_libro(codice: str, titolo: str, autore: str, anno_pubblicazione: int) -> dict | str
Aggiunge un nuovo libro alla biblioteca.
Se il codice è già presente, restituisce:
"Errore, libro già registrato."

* rimuovi_libro(codice: str) -> dict | str
Rimuove un libro dalla biblioteca.
Se il codice non esiste, restituisce:
"Errore, libro non trovato."

* segna_non_disponibile(codice: str) -> dict | str
Imposta "disponibile": False (ad esempio, se il libro è stato preso in prestito).
Se il codice non esiste, restituisce:
"Errore, libro non trovato."

* segna_disponibile(codice: str) -> dict | str
Imposta "disponibile": True.
Se il codice non esiste, restituisce:
"Errore, libro non trovato."

* aggiorna_titolo(codice: str, nuovo_titolo: str) -> dict | str
Aggiorna il titolo di un libro.
Se il codice non esiste, restituisce:
"Errore, libro non trovato."

* aggiorna_autore(codice: str, nuovo_autore: str) -> dict | str
Aggiorna l’autore di un libro.
Se il codice non esiste, restituisce:
"Errore, libro non trovato."

* mostra_libro(codice: str) -> dict | str
Mostra le informazioni di un libro specifico.
Se il codice non esiste, restituisce:
"Errore, libro non trovato."

* lista_libri() -> list[str]
Restituisce la lista di tutti i codici dei libri presenti nella biblioteca.

* lista_disponibili() -> dict[str, dict]
Restituisce solo i libri con "disponibile": True.
'''
class GestoreBiblioteca:
    def __init__(self):
        self.libri: dict[str, dict] = {}
    
    def aggiungi_libro(self, codice: str, titolo:str, autore: str, anno_pubblicazione: int) -> dict|str:
        if codice in self.libri:
            return "Errore, libro già registrato."
        self.libri[codice] = {"titolo": titolo, "autore": autore, "anno_pubblicazione": anno_pubblicazione, "disponibile": True}

        return {codice: self.libri[codice]}
    
    def rimuovi_libro(self, codice: str) -> dict|str:
        if codice not in self.libri:
            return "Errore, libro non trovato."
        libro_rimosso = self.libri.pop(codice)

        return {codice: libro_rimosso}
    
    def segna_non_disponibile(self, codice: str) -> dict|str:
        if codice not in self.libri:
            return "Errore, libro non trovato."
        self.libri[codice]["disponibile"] = False

        return {codice: self.libri[codice]}
    
    def segna_disponibile(self, codice: str) -> dict|str:
        if codice not in self.libri:
            return "Errore, libro non trovato."
        self.libri[codice]["disponibile"] = True

        return {codice: self.libri[codice]}

    def aggiorna_titolo(self, codice: str, nuovo_titolo: str) -> dict|str:
        if codice not in self.libri:
            return "Errore, libro non trovato."
        self.libri[codice]["titolo"] = nuovo_titolo

        return {codice: self.libri[codice]}
    
    def aggiorna_autore(self, codice: str, nuovo_autore: str) -> dict|str:
        if codice not in self.libri:
            return "Errore, libro non trovato."
        self.libri[codice]["autore"] = nuovo_autore

        return {codice: self.libri[codice]}
    
    def mostra_libro(self, codice: str) -> dict|str:
        if codice not in self.libri:
            return "Errore, libro non trovato."
        return {codice: self.libri[codice]}

    def lista_libri(self) -> list[str]:
        return list(self.libri.keys())

    def lista_disponibili(self) -> dict[str, dict]:
        return {codice: info for codice, info in self.libri.items() if info["disponibile"]}

