'''
Esercizio 1
Tema: Incapsulamento e gestione attributi
Obiettivo: Creare una classe Studente con attributi privati e getter/setter.

Traccia:

    * Crea una classe Studente con nome e voto.
    * Entrambi gli attributi devono essere privati.
    * Implementa:

        * get_nome() e set_nome(nome)
        * get_voto() e set_voto(voto) (controlla che il voto sia tra 0 e 10, altrimenti lancia ValueError)

Suggerimento:

    * Usa self.__nome e self.__voto per gli attributi privati.
'''
# Versione sbagliata
class Studente:
    def __init__(self, nome: str, voto: int):
        self.__nome = nome
        self.__voto = voto
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_voto(self) -> int:
        return self.__voto
    
    def set_nome(self, nome: str):
        self.__nome = nome
    
    def set_voto(self, voto: int):
        if voto < 0 or voto > 10:
            raise ValueError("Errore, il voto inserito non è compreso tra 0 e 10") 
        self.__voto = voto

'''
    * Qui l’__init__ assegna direttamente gli attributi privati senza passare dai setter.
    * Funziona, ma non applica la logica di validazione definita in set_voto.
    * Quindi se fai Studente("Luca", 15), l’oggetto viene creato anche se il voto non è valido.
'''

# Versione giusta
class Studente:
    def __init__(self, nome: str, voto: int):
        self.set_nome(nome)
        self.set_voto(voto)
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_voto(self) -> int:
        return self.__voto
    
    def set_nome(self, nome: str):
        self.__nome = nome
    
    def set_voto(self, voto: int):
        if voto < 0 or voto > 10:
            raise ValueError("Errore, il voto inserito non è compreso tra 0 e 10") 
        self.__voto = voto
    
    def __str__(self):
        return f"Nome: {self.__nome}, Voto: {self.__voto}"

'''
    * Qui l’__init__ usa i setter.
    * La validazione del voto viene applicata subito: se il voto non è tra 0 e 10, viene lanciato un ValueError.
    * Questo è più sicuro e corretto in termini di incapsulamento e validazione.
'''

studente1 = Studente("Lola", 5)
studente2 = Studente("Fran", 9)
print(studente1)
print(studente2)