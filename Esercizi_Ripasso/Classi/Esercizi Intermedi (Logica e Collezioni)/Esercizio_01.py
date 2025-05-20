# Esercizio 1
'''
Classe Studente
Crea una classe Studente con:

Attributi: nome, cognome, voti (lista vuota)

Metodi:

aggiungi_voto(voto)

media_voti() → restituisce la media

stampa_info() → stampa nome completo e media
'''

class Studente:

    def __init__(self, nome:str, cognome:str, voti:list[int]):
        self.nome = nome
        self.cognome = cognome
        self.voti = voti
    
    def aggiungi_voto(self, voto):
        self.voti.append(voto)
    
    def media_voti(self):
        return sum(self.voti) / len(self.voti) if len(self.voti) > 0 else 0
    
    def stampa_info(self):
        print(f"Nome: {self.nome} {self.cognome}\nMedia Voti: {self.media_voti()}")

studente = Studente("Nico", "Rojas", [20, 28, 29, 27, 30])
studente.stampa_info()
        