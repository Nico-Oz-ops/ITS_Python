'''
Esercizio 13 - Gioco di Carte (Classe Carta)

Tema: Classe con proprietà calcolate e validazioni tramite @property.
Obiettivo: Creare una carta da gioco con valore e seme, con proprietà che calcolano il punteggio e se la carta è alta.

Traccia:

1. Crea una classe Carta con attributi:

    * valore (numero intero da 1 a 13)
    * seme (stringa: “cuori”, “quadri”, “fiori”, “picche”)

2. Usa @property per:

    * valore → getter e setter con validazione (1-13)
    * seme → getter e setter con validazione (solo i quattro semi validi)

3. Aggiungi proprietà calcolate:

    * punteggio → 10 per 11, 12, 13; altrimenti uguale al valore
    * alta → True se il valore è ≥ 11, False altrimenti

4. Aggiungi __str__ per stampare in modo leggibile la carta:
    Esempio: "Carta: 12 di cuori, punteggio 10, alta: True"

Suggerimento:

* Usa _valore e _seme come attributi interni.
* Le proprietà calcolate (punteggio e alta) devono essere solo getter, senza setter.
'''

class Carta:
    def __init__(self, valore: int, seme: str):
        self.valore = valore
        self.seme = seme
    
    @property
    def valore(self):
        return self._valore
    
    @valore.setter
    def valore(self, valore: int):
        if not isinstance(valore, int) or valore < 1 or valore > 13:
            raise ValueError("Valore non valido.")
        self._valore = valore
    
    @property
    def seme(self):
        return self._seme
    
    @seme.setter
    def seme(self, seme: str):
        semi = ["cuori", "quadri", "fiori", "picche"]
        if not isinstance(seme, str) or seme.strip() == "" or seme.strip() not in semi:
            raise ValueError("Seme non valido.")
        self._seme = seme
    
    @property
    def punteggio(self):
        if self.valore >= 11:
            return 10
        else:
            return self.valore
    
    @property
    def alta(self):
        return self.valore >= 11
    
    def __str__(self):
        return f"Carta: {self.valore} di {self.seme}, punteggio {self.punteggio}, alta: {self.alta}"

carta1 = Carta(11, "picche")
print(carta1)

print("-" * 25)

carta2 = Carta(7, "cuori")
print(carta2)

print("-" * 25)

try:
    carta3 = Carta(14, "quadri")
    print(carta3)

except ValueError as error:
    print(error)