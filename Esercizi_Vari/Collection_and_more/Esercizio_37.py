'''
Tema: Dizionari - Massimo valore
Obiettivo: Trovare l’elemento con il punteggio più alto.

Nome dell’esercizio: Studente migliore

Traccia:
Scrivi una funzione studente_migliore(studenti: dict[str, int]) -> tuple[str, int] che, 
dato un dizionario studenti con nome → voto, ritorni una tupla contenente il nome e il 
voto dello studente con il punteggio più alto.

studenti = {
    "Marco": 25,
    "Luca": 18,
    "Anna": 30,
    "Giulia": 27,
    "Paolo": 22
}

Suggerimento:
Puoi usare un ciclo per confrontare i voti, oppure la funzione max() con una chiave.
'''
# Alternativa 1
def studente_migliore(studenti: dict[str, int]) -> tuple[str, int]:
    nome_voto_piu_alto = max(studenti, key=lambda nome: studenti[nome]) # trova il nome con il voto più alto
    return (nome_voto_piu_alto, studenti[nome_voto_piu_alto])

studenti = {
    "Marco": 25,
    "Luca": 18,
    "Anna": 30,
    "Giulia": 27,
    "Paolo": 22
}
print(studente_migliore(studenti))

# Alternativa 2
def studente_migliore(studenti: dict[str, int]) -> tuple[str, int]:
    nome_max = None
    voto_max = 0

    for nome, voto in studenti.items():
        if voto > voto_max:
            voto_max = voto
            nome_max = nome
    
    return (nome_max, voto_max) 

studenti = {
    "Marco": 25,
    "Luca": 18,
    "Anna": 30,
    "Giulia": 27,
    "Paolo": 22
}
print(studente_migliore(studenti))