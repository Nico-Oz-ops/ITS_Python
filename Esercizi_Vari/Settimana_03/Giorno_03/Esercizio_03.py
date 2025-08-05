'''
Tema: Dizionari annidati, calcolo di massimi, trasformazioni dati.
Obiettivo: Trovare, per ogni materia, lo studente con la media più alta.
'''

# Esercizio 03
# Titolo: "migliore_per_materia"

'''
Traccia:
Hai un dizionario che contiene, per ogni studente, un dizionario di materie e una lista di voti per ciascuna materia:

studenti = {
    "Anna": {"matematica": [28, 30, 25], "storia": [30, 21, 25], "filosofia": [25, 26, 29]},
    "Luca": {"matematica": [18, 29, 30], "storia": [24, 28, 27], "filosofia": [27, 19, 26]},
    "Marta": {"matematica": [22, 23, 25], "storia": [19, 21, 0], "filosofia": []},
}

Scrivi una funzione migliore_per_materia(studenti: dict[str, dict[str, list[int]]]) -> dict[str, tuple[list[str], float]]
che restituisce, per ogni materia, la media più alta e il nome o i nomi degli studenti che l’hanno ottenuta.

{
    'matematica': (['Anna'], 27.67),
    'storia': (['Luca'], 26.33),
    'filosofia': (['Anna'], 26.67)
}

Se più studenti hanno la stessa media massima in una materia, includili tutti.
'''

def migliore_per_materia(studenti: dict[str, dict[str, list[int]]]) -> dict[str, tuple[list[str], float]]:
    migliori = {}

    for studente, materie in studenti.items():
        for materia, voti in materie.items():
            voti_media = round((sum(voti) / len(voti)), 2) if voti else 0

            if materia not in migliori:
                migliori[materia] = ([studente], voti_media)

            else:
                voto_medio_attuale = migliori[materia][1]

                if voti_media > voto_medio_attuale:
                    migliori[materia] = ([studente], voti_media)

                elif voti_media == voto_medio_attuale:
                    migliori[materia][0].append(studente)

    return migliori

studenti = {
    "Anna": {"matematica": [28, 30, 25], "storia": [30, 21, 25], "filosofia": [25, 26, 29]},
    "Luca": {"matematica": [18, 29, 30], "storia": [24, 28, 27], "filosofia": [27, 19, 26]},
    "Marta": {"matematica": [22, 23, 25], "storia": [19, 21, 0], "filosofia": []},
}

print(migliore_per_materia(studenti))
                

