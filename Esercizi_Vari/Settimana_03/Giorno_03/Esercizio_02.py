'''
Tema: Trasformazione dati con dizionari annidati
Obiettivo: Calcolare un valore aggregato da una struttura complessa
'''

# Esercizio 02
# Titolo: "Media voti per studente"

'''
Traccia:
Hai una struttura dati come questa:

studenti = {
    "Anna": {"matematica": 28, "storia": 30, "filosofia": 25},
    "Luca": {"matematica": 18, "storia": 24, "filosofia": 27},
    "Marta": {"matematica": 22, "storia": 19, "filosofia": 20},
}

Scrivi una funzione media_per_studente(studenti: dict) -> dict[str, float]
che restituisce un dizionario in cui:

* ogni chiave è il nome dello studente
* ogni valore è la media dei suoi voti (arrotondata a 2 cifre decimali)

Suggerimento
Puoi usare:

* .items() per scorrere studenti,
* sum(...) / len(...) per calcolare la media dei voti,
* una dictionary comprehension per costruire il risultato.
'''

def media_per_studente(studenti: dict[str, dict[str, int]]) -> dict[str, float]:
    return {studente: round(sum(voti.values()) / len(voti), 2) for studente, voti in studenti.items()}

studenti = {
    "Anna": {"matematica": 28, "storia": 30, "filosofia": 25},
    "Luca": {"matematica": 18, "storia": 24, "filosofia": 27},
    "Marta": {"matematica": 22, "storia": 19, "filosofia": 20},
}

print(media_per_studente(studenti))


def media_materia_per_studente(studenti: dict[str, dict[str, int]]) -> dict[str, dict[str, float]]:
    return {studente: {materia: round(sum(voti) / len(voti), 2) if voti else 0 for materia, voti in materie.items()} 
                    for studente, materie in studenti.items()} 

studenti = {
    "Anna": {"matematica": [28, 30, 25], "storia": [30, 21, 25], "filosofia": [25, 26, 29]},
    "Luca": {"matematica": [18, 29, 30], "storia": [24, 28, 27], "filosofia": [27, 19, 26]},
    "Marta": {"matematica": [22, 23, 25], "storia": [19, 21, 0], "filosofia": []},
}

print(media_materia_per_studente(studenti))

























# def media_per_studente(studenti: dict[dict]) -> dict[str, float]:
#     return {nome: round(sum(voti.values()) / len(voti), 2) for nome, voti in studenti.items()}

# studenti = {
#     "Anna": {"matematica": 28, "storia": 30, "filosofia": 25},
#     "Luca": {"matematica": 18, "storia": 24, "filosofia": 27},
#     "Marta": {"matematica": 22, "storia": 19, "filosofia": 20},
# }

# print(media_per_studente(studenti))


# # E se volessi conoscere i voti di una sola materia? 
# def voti_studente_materia(studenti: dict[dict], materia: str) -> dict[str, float]:
#     return {nome: voti.get(materia, 0) for nome, voti in studenti.items()}

# studenti = {
#     "Anna": {"matematica": 28, "storia": 30, "filosofia": 25},
#     "Luca": {"matematica": 18, "storia": 24, "filosofia": 27},
#     "Marta": {"matematica": 22, "storia": 19, "filosofia": 20},
# }

# print(voti_studente_materia(studenti, "storia"))
# print(voti_studente_materia(studenti, "matematica"))
# print(voti_studente_materia(studenti, "filosofia"))