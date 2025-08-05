'''Hai un dizionario che rappresenta gli studenti e i loro voti in varie 
materie. Scrivi una funzione che restituisce, per ogni materia, il nome 
dello studente con il voto più alto.
 
studenti = {
    "Anna": {"matematica": 28, "storia": 30, "inglese": 25},
    "Luca": {"matematica": 28, "storia": 27, "inglese": 30},
    "Marta": {"matematica": 26, "storia": 29, "inglese": 30},
}
'''

def migliori_studenti_materia(studenti: dict[str, dict[str, int]]) -> dict[str, tuple[list[str], int]]:

    migliore_studente = {}

    for studente, voti in studenti.items():
        for materia, voto in voti.items():
            if materia not in migliore_studente:
                migliore_studente[materia] = ([studente], voto)
            else:
                voto_attuale = migliore_studente[materia][1]

                if voto > voto_attuale:
                    migliore_studente[materia] = ([studente], voto)
                
                elif voto == voto_attuale:
                    migliore_studente[materia][0].append(studente)
        
    return migliore_studente
    
    # return {materia: (studenti_voto_massimo, voto_massimo) for materia, (studenti_voto_massimo, voto_massimo) in migliore_studente.items()}

studenti = {
    "Anna": {"matematica": 28, "storia": 30, "inglese": 25},
    "Luca": {"matematica": 28, "storia": 27, "inglese": 30},
    "Marta": {"matematica": 26, "storia": 29, "inglese": 30},
}

print(migliori_studenti_materia(studenti))

















































#     migliori_studenti = {}

#     for studente, voti in studenti.items():
#         for materia, voto in voti.items():
#             if materia not in migliori_studenti or voto > migliori_studenti[materia][1]:
#                 migliori_studenti[materia] = (studente, voto)
    
#     return {materia: (studente, voto) for materia, (studente, voto) in migliori_studenti.items()}


# studenti = {
#     "Anna": {"matematica": 28, "storia": 30, "inglese": 25},
#     "Luca": {"matematica": 30, "storia": 27, "inglese": 29},
#     "Marta": {"matematica": 26, "storia": 30, "inglese": 30},
# }

# print(migliori_studenti_materia(studenti))