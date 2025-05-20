# Esercizio 4
'''
Classe Contatto + Rubrica
Contatto: nome, telefono

Rubrica:

Attributo: lista di contatti

Metodi:

aggiungi_contatto(contatto)

cerca(nome)

mostra_tutti()
'''

class Contatto:

    def __init__(self, nome:str, telefono:int):
        self.nome = nome
        self.telefono = telefono
    
class Rubrica:

    def __init__(self, contatti:list[Contatto]):
        self.contatti = contatti
    
    def aggiungi_contatto(self, contatto:Contatto):
        self.contatti.append(contatto)
    
    def cerca(self, nome:str):
        for contatto in self.contatti:
            if contatto.nome.lower() == nome.lower():
                print(f"Contatto trovato!\nNome: {contatto.nome} - Tel: {contatto.telefono}")
                return
            
        print(f"Il contatto '{nome}' non è stato trovato")

    def mostra_tutti(self):
        print("\nI contatti nella rubrica sono:\n")

        for i, contatto in enumerate(self.contatti, 1):
            print(f"{i} - Nome: {contatto.nome} - Tel: {contatto.telefono}")

contatto_1 = Contatto("Nico", 3664823257)
contatto_2 = Contatto("Benja", 3334823256)

rubrica = Rubrica([contatto_1])
rubrica.aggiungi_contatto(contatto_2)
rubrica.mostra_tutti()
rubrica.cerca("paloma")



        
        