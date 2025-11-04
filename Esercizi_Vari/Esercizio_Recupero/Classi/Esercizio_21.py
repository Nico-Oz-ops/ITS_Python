'''
Esercizio: RubricaTelefonica

Crea una classe per gestire una semplice rubrica di contatti.

Classe RubricaTelefonica

A. Attributi:
* contatti: dict[str, dict]
Ogni chiave è il nome del contatto, e il valore è un dizionario con:
{
"telefono": str,
"email": str,
"preferito": bool
}

B. Metodi:

* aggiungi_contatto(nome: str, telefono: str, email: str) -> dict | str
Aggiunge un nuovo contatto alla rubrica.
Se il contatto con lo stesso nome esiste già, restituisce:
"Errore, contatto già registrato."

* rimuovi_contatto(nome: str) -> dict | str
Rimuove un contatto esistente.
Se il contatto non esiste, restituisce:
"Errore, contatto non trovato."

* aggiorna_numero(nome: str, nuovo_numero: str) -> dict | str
Aggiorna il numero di telefono di un contatto.
Se il contatto non esiste, restituisce:
"Errore, contatto non trovato."

* aggiorna_email(nome: str, nuova_email: str) -> dict | str
Aggiorna l’email di un contatto.
Se il contatto non esiste, restituisce:
"Errore, contatto non trovato."

* segna_preferito(nome: str) -> dict | str
Imposta il contatto come preferito ("preferito": True).
Se il contatto non esiste, restituisce:
"Errore, contatto non trovato."

* rimuovi_preferito(nome: str) -> dict | str
Imposta il contatto come non preferito ("preferito": False).
Se il contatto non esiste, restituisce:
"Errore, contatto non trovato."

* mostra_contatto(nome: str) -> dict | str
Restituisce tutte le informazioni di un contatto.
Se il contatto non esiste, restituisce:
"Errore, contatto non trovato."

* lista_contatti() -> list[str]
Restituisce la lista di tutti i nomi dei contatti presenti nella rubrica.

* lista_preferiti() -> dict[str, dict]
Restituisce solo i contatti con "preferito": True.
'''

class RubricaTelefonica:
    def __init__(self):
        self.contatti: dict[str, dict] = {}

    def aggiungi_contatto(self, nome: str, telefono: str, email: str) -> dict|str:
        if nome not in self.contatti:
            self.contatti[nome] = {"telefono": telefono, "email": email, "preferito": False}
            return {nome: self.contatti[nome]}
        
        return "Errore, contatto già registrato" 
    
    def rimuovi_contatto(self, nome: str) -> dict|str:
        if nome not in self.contatti:
            return "Errore, contatto non trovato"
        contatto_rimosso = self.contatti.pop(nome)

        return {nome: contatto_rimosso}
    
    def aggiorna_numero(self, nome: str, nuovo_numero: str) -> dict|str:
        if nome not in self.contatti:
            return "Errore, contatto non trovato"
        self.contatti[nome]["telefono"] = nuovo_numero

        return {nome: self.contatti[nome]}
    
    def aggiorna_email(self, nome: str, nuova_email: str) -> dict|str:
        if nome not in self.contatti:
            return "Errore, contatto non trovato"
        self.contatti[nome]["email"] = nuova_email

        return {nome: self.contatti[nome]}
    
    def segna_preferito(self, nome: str) -> dict|str:
        if nome not in self.contatti:
            return "Errore, contatto non trovato"
        self.contatti[nome]["preferito"] = True

        return {nome: self.contatti[nome]}
    
    def rimuovi_preferito(self, nome: str) -> dict|str:
        if nome not in self.contatti:
            return "Errore, contatto non trovato"
        self.contatti[nome]["preferito"] = False

        return {nome: self.contatti[nome]}

    def mostra_contatto(self, nome: str) -> dict|str:
        if nome not in self.contatti:
            return "Errore, contatto non trovato"
        return {nome: self.contatti[nome]}
    
    def lista_contatti(self) -> list[str]:
        return list(self.contatti.keys())
    
    def lista_preferiti(self) -> dict[str, dict]:
        return {nome: info for nome, info in self.contatti.items() if info["preferito"]}



# Test
rubrica = RubricaTelefonica()

rubrica.aggiungi_contatto("Alice", "3456789012", "alice@mail.com")
rubrica.aggiungi_contatto("Marco", "3201234567", "marco@mail.com")

rubrica.segna_preferito("Alice")

print(rubrica.mostra_contatto("Alice"))
# {'telefono': '3456789012', 'email': 'alice@mail.com', 'preferito': True}

print(rubrica.lista_contatti())
# ['Alice', 'Marco']

print(rubrica.lista_preferiti())
# {'Alice': {'telefono': '3456789012', 'email': 'alice@mail.com', 'preferito': True}}