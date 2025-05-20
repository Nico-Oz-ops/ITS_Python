# Esercizio 01

'''
1) crea un file json usando i comandi touch e nano. Leggete il file appena creato e stampate un valore.
2) crea un file json da Python salvando un dizionario a vostra scelta.
3) crea un file json usando touch e nano che contenga codici fiscali come chiavi e come valori dizionari 
che contengono nome, cognome, età della persona (almeno due persone) e modificare il json aggiungendo una persona.
'''

import json


PATH: str = "ESERCIZI_DATA/Lezione_15/persone.json"
mode: str = "w"
config: dict = {}

with open(PATH, mode='r') as file:
    config = json.load(file)
    print(config["VLRMLX77T21Z601P"]["nome"])



# persone = {
#     "VLRMLX77T21Z601P": {
#         "nome": "Mario",
#         "cognome": "Rossi",
#         "età": 35
#         },
    
#     "MWQASD88Y32O745A": {
#         "nome": "Nico",
#         "cognome": "Landa",
#         "età": 25
#         }
# }
# PATH: str = "ESERCIZI_DATA/Lezione_15/persone.json"
# with open(PATH, 'w') as file:
#     json.dump(persone, file, indent=4)
