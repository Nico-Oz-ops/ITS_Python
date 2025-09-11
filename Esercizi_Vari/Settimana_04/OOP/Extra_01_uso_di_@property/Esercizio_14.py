'''
Esercizio 14 - Studente con Bonus

Tema: Classe avanzata con proprietà calcolate e metodi collegati tra loro.
Obiettivo: Creare una classe StudenteAvanzato che gestisce voti, media, stato promosso e bonus extra.

Traccia:

1. Crea una classe StudenteAvanzato con attributi:

    * nome (stringa non vuota)
    * voti (lista di numeri 0-10)
    * bonus (numero ≥ 0, default 0)

2. Usa @property per:

    * media → calcola la media dei voti + bonus
    * promosso → True se media ≥ 6, altrimenti False
    * ha_bonus → True se bonus > 0

3. Aggiungi metodi per:

    * aggiungi_voto(voto) → aggiunge un voto valido alla lista
    * aggiungi_bonus(punti) → aumenta il bonus se punti ≥ 0

4. Aggiungi __str__ per stampare:

    * Nome, media, promosso e se ha bonus

Suggerimento:

* Usa _nome, _voti, _bonus come attributi interni.
* Tutti i controlli devono sollevare ValueError se i valori non sono validi.
* Le proprietà media, promosso e ha_bonus devono essere solo getter.
'''

class StudenteAvanzato:
    def __init__(self, nome: str, bonus: int, voti: list[int] = None):
        self.nome = nome
        self.bonus = bonus
        self.voti = voti if voti is not None else []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str) or nome.strip() == "":
            raise ValueError("Nome non valido")
        self._nome = nome
    
    @property
    def bonus(self):
        return self._bonus
    
    @bonus.setter
    def bonus(self, bonus: int):
        if not isinstance(bonus, int) or bonus < 0:
            raise ValueError("Bonus non valido")
        self._bonus = bonus
    
    @property
    def voti(self):
        return self._voti
    
    @voti.setter
    def voti(self, voti: list[int]):
        for voto in voti: # serve a validare l'intera lista quando viene assegnata
            if not isinstance(voto, int) or voto < 0 or voto > 10:
                raise ValueError("Voto non valido")
        self._voti = voti
    
    @property
    def media(self):
        if self.voti == []:
            raise ValueError("Lista dei voti è vuota, non si può calcolare la media")
        return (sum(self.voti) / len(self.voti)) + self.bonus
    
    @property
    def promosso(self):
        return self.media >= 6
    
    @property
    def ha_bonus(self):
        return self.bonus > 0
    
    def aggiungi_voto(self, voto: int): #serve a validare ogni singolo voto quando viene aggiunto uno alla volta
        if not isinstance(voto, int) or voto < 0 or voto > 10:
            raise ValueError("Voto non valido")
        self.voti.append(voto)
    
    def aggiungi_bonus(self, punti: int):
        if not isinstance(punti, int) or punti < 0:
            raise ValueError("Punti non validi")
        self.bonus += punti
    
    def __str__(self):
        return f"Nome: {self.nome}\nMedia: {self.media}\nPromosso: {self.promosso}\nBonus: {self.bonus}"


studente1 = StudenteAvanzato("Javi", 0, [])


studente1.aggiungi_voto(8)
studente1.aggiungi_voto(9)
print(studente1)

print(f"Lo studente ha bonus? {studente1.ha_bonus}")

print("-" * 20)

studente1.aggiungi_bonus(2)
print(f"Lo studente ha bonus? {studente1.ha_bonus}")

print(studente1)