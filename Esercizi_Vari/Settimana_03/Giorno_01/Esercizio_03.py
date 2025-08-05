'''
Tema: Manipolazione di strutture dati annidate.
Obiettivo: 
'''

# Esercizio 03
# Titolo: "Trasformare un dizionario di liste in una lista di dizionari"

'''
Traccia:
Hai un dizionario dove ogni chiave è associata a una lista di valori 
(esempio: corsi e voti). Devi creare una lista di dizionari, dove ogni dizionario 
rappresenta un "record" con i dati combinati da tutte le liste.
'''

def trasforma_dizionario(dati: dict) -> list[dict]:

    result = []
    n = len(dati["nome"])

    for i in range(n):
        record = {
            "nome": dati["nome"][i],
            "corso": dati["corso"][i],
            "voto": dati["voto"][i]
        }
        result.append(record)
    return result

dati = {
    "nome": ["Anna", "Luca", "Marco"],
    "corso": ["Fisica", "Matematica", "Informatica"],
    "voto": [28, 22, 30]
}

print(trasforma_dizionario(dati))


# Variante, uso di zip()
def trasforma_dizionario(dati: dict) -> list[dict]:
    return [
        {"nome": nome, "corso": corso, "voto": voto}
        for nome, corso, voto in zip(dati["nome"], dati["corso"], dati["voto"])
    ]

dati = {
    "nome": ["Anna", "Luca", "Marco"],
    "corso": ["Fisica", "Matematica", "Informatica"],
    "voto": [28, 22, 30]
}

print(trasforma_dizionario(dati))


# Variante, da lista a dizionario
def trasforma_lista(dati: list[dict]) -> dict[list]:
    risultato = {
        "nome": [],
        "corso": [],
        "voto": []
        }
    
    for elemento in dati:
        risultato["nome"].append(elemento["nome"])
        risultato["corso"].append(elemento["corso"])
        risultato["voto"].append(elemento["voto"])

    return risultato

dati = [
    {"nome": "Anna", "corso": "Fisica", "voto": 28},
    {"nome": "Luca", "corso": "Matematica", "voto": 22},
    {"nome": "Marco", "corso": "Informatica", "voto": 30}
]

print(trasforma_lista(dati))


