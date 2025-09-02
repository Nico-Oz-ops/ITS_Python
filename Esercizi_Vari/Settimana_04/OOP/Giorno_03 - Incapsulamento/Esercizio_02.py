'''
Esercizio 2 - Gestione conto bancario

Tema: Attributi privati, getter/setter e metodi di controllo
Obiettivo: Creare una classe ContoBancario con sicurezza e validazione

Traccia:

Crea una classe ContoBancario con attributi privati:

    * __intestatario (stringa)
    * __saldo (float, inizialmente 0)

Implementa metodi:

    * get_intestatario() → ritorna il nome
    * get_saldo() → ritorna il saldo
    * deposita(importo) → aggiunge soldi al saldo (importo > 0, altrimenti ValueError)
    * preleva(importo) → sottrae soldi dal saldo se sufficiente, altrimenti ValueError
    * set_intestatario(nome) → permette di modificare il nome dell’intestatario

Suggerimento:

    * Usa self.__saldo e self.__intestatario come attributi privati.
    * Controlla sempre che l’importo sia positivo e il saldo sufficiente prima di prelevare.
'''

class ContoBancario:
    def __init__(self, intestatario: str, saldo: float = 0):
        self.set_intestatario(intestatario)     # usa setter per eventuale validazione
        self.__saldo = saldo                    # saldo iniziale privato, senza controlli

    def get_intestatario(self) -> str:
        return self.__intestatario
    
    def get_saldo(self) -> float:
        return self.__saldo
    
    def set_intestatario(self, intestatario: str):
        if not isinstance(intestatario, str) or intestatario.strip() == "": # strip() rimuove spazi all’inizio/fine e previene nomi solo con spazi.
            raise ValueError("Errore, nome non valido")
        self.__intestatario = intestatario
    
    def deposita(self, importo: float):
        if not isinstance(importo, (float, int)) or importo <= 0:
            raise ValueError("Errore, importo non valido")
        self.__saldo += importo
    
    def preleva(self, importo: float):
        if not isinstance(importo, (int, float)) or importo <= 0:
            raise ValueError("Errore, importo di prelievo non valido")
        
        if importo > self.__saldo:
            raise ValueError("Errore, l'importo del prelievo è superiore al saldo attuale")
        
        self.__saldo -= importo
    
    def __str__(self):
        return f"Intestatario: {self.__intestatario}\nSaldo: {self.__saldo}"

cb = ContoBancario("Nico")
cb.deposita(2500)
print(cb)
print("-" * 50)
cb.preleva(500)
print(cb)


    

        