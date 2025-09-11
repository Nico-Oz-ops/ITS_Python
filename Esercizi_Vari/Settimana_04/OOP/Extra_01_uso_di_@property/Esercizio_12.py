'''
Esercizio 12 - Studente con media e promozione

Tema: Attributi calcolati dinamicamente e validazioni con @property.
Obiettivo: Creare una classe Studente che gestisca voti e calcoli automatici della media e 
dello stato di promozione.

Traccia:

1. Crea una classe Studente con gli attributi:

    * nome (stringa non vuota)
    * voti (lista di numeri da 0 a 10)

2. Usa @property per:

    * media → calcola la media dei voti
    * promosso → restituisce True se la media ≥ 6, altrimenti False

3. Gestisci i setter in modo che:

    * nome non possa essere vuoto
    * i voti inseriti siano numeri validi tra 0 e 10

4. Aggiungi __str__ per stampare:

    * nome, voti, media e se lo studente è promosso o bocciato

Suggerimento:

* La proprietà media non ha bisogno di setter, perché è calcolata automaticamente dai voti.
* La proprietà promosso dipende dalla media e quindi può essere solo getter.
'''

class Studente:
    def __init__(self, nome: str, voti: list[int] = None):
        self.nome = nome
        self.voti = voti if voti is not None else []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome non valido.")
        self._nome = nome
    
    @property
    def voti(self):
        return self._voti
    
    @voti.setter
    def voti(self, voti: list[int]):
        for voto in voti:
            if not isinstance(voto, (int, float)) or voto < 0 or voto > 10:
                raise ValueError("Voto non valido.")
        self._voti = voti
    
    @property
    def media(self):
        if self.voti == []:
            raise ValueError("Lista vuota")
        return sum(self.voti) / len(self.voti)
    
    @property
    def promosso(self):
        return self.media >= 6 # opzione più pythonica, piuttosto che usare if (true) / else(false)
    
    def __str__(self):
        return f"**Dati studente**\nNome: {self.nome}\nMedia dei voti: {self.media}\nPromosso: {self.promosso}"

studente1 = Studente("Pedro", [9, 7, 9, 9])
studente2 = Studente("Mike", [5, 8, 7, 6])

print(studente1)
print("-" * 30)
print(studente2)
print("-" * 30)

try:
    studente3 = Studente("Nicol", [0, -9, 7, 10])
    print(studente3)

except ValueError as error:
    print(error)
