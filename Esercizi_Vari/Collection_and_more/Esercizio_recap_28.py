'''
Tema: Dizionari annidati + comprehension
Obiettivo: Filtrare da strutture più complesse.

Nome: Filtra studenti promossi (annidati + comprehension)

Traccia:
Data una struttura tipo:

studenti = {
    "Marco": {"eta": 20, "voto": 28},
    "Luca": {"eta": 22, "voto": 18},
    "Anna": {"eta": 19, "voto": 30},
    "Mario": {"eta": 25, "voto": 27},
    "Carlotta": {"eta": 20, "voto": 26},
    "Giuseppe": {"eta": 18, "voto": 20},
}

Scrivi una funzione studenti_promossi(studenti) che ritorni una lista con 
i nomi degli studenti che hanno almeno 21 anni e che hanno voto ≥ 18, usando dictionary/list comprehension.
'''
# Alternativa 1
def studenti_promossi(studenti: dict[str, dict[int, int]], soglia_eta: int, soglia_voto: int) -> list[str]:
    risultato = []

    for nome in studenti:
        if nome in studenti:
            if studenti[nome]["eta"] >= soglia_eta and studenti[nome]["voto"] >= soglia_voto:
                risultato.append(nome)

    return risultato

studenti = {
    "Marco": {"eta": 20, "voto": 28},
    "Luca": {"eta": 22, "voto": 18},
    "Anna": {"eta": 19, "voto": 30},
    "Mario": {"eta": 25, "voto": 27},
    "Carlotta": {"eta": 20, "voto": 26},
    "Giuseppe": {"eta": 18, "voto": 20},
}
print(studenti_promossi(studenti, 21, 18))

# Alternativa 2
def studenti_promossi(studenti: dict[str, dict[int, int]], soglia_eta: int, soglia_voto: int) -> list[str]:
    return [nome for nome in studenti if studenti[nome]["eta"] >= soglia_eta and studenti[nome]["voto"] >= soglia_voto]

studenti = {
    "Marco": {"eta": 20, "voto": 28},
    "Luca": {"eta": 22, "voto": 18},
    "Anna": {"eta": 19, "voto": 30},
    "Mario": {"eta": 25, "voto": 27},
    "Carlotta": {"eta": 20, "voto": 26},
    "Giuseppe": {"eta": 18, "voto": 20},
}
print(studenti_promossi(studenti, 21, 18))

# Alternativa 3
def studenti_promossi(studenti: dict[str, dict[int, int]], soglia_eta: int, soglia_voto: int) -> list[str]:
    sopra_soglie = filter(lambda nome: studenti[nome]["eta"] >= soglia_eta 
                              and studenti[nome]["voto"] >= soglia_voto, studenti)

    return list(sopra_soglie)

studenti = {
    "Marco": {"eta": 20, "voto": 28},
    "Luca": {"eta": 22, "voto": 18},
    "Anna": {"eta": 19, "voto": 30},
    "Mario": {"eta": 25, "voto": 27},
    "Carlotta": {"eta": 20, "voto": 26},
    "Giuseppe": {"eta": 18, "voto": 20},
}
print(studenti_promossi(studenti, 21, 18))