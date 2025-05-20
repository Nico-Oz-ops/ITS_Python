# Esercizio 5
'''
Classe Auto
Classe Auto con:

Attributi: marca, modello, anno

Metodo: scheda() che stampa:

"Auto: Fiat Panda (2010)"
'''

class Auto:

    def __init__(self, marca:str, modello:str, anno:int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def scheda(self):
        print(f"Auto: {self.marca} {self.modello} ({self.anno})")

auto = Auto("Fiat", "Panda", 2010)
auto.scheda()


# Variante

'''
Esercizio: Gestione di una lista di auto
Obiettivo:
Crea 3 oggetti Auto con marche, modelli e anni diversi.

Inseriscili in una lista chiamata parco_auto.

Scorri la lista e stampa le schede di tutte le auto usando un ciclo.
'''

class Auto:

    def __init__(self, marca:str, modello:str, anno:int):
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def scheda(self):
        print(f"Auto: {self.marca} {self.modello} ({self.anno})")

# 3 oggetti auto
auto_1 = Auto("Fiat", "Panda", 2010)
auto_2 = Auto("Volkswagen", "Golf", 2015)
auto_3 = Auto("Tesla", "Model 3", 2022)

# inserire gli oggetti nella lista
parco_auto = [auto_1, auto_2, auto_3]

# stampare tutte le schede (usando un ciclo)
for auto in parco_auto:
    auto.scheda()
        