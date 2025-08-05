'''
Tema: Lavorare con dizionari annidati e manipolazione di dati aggregati.

Obiettivo: Scrivere una funzione che, data la struttura dati degli studenti 
con materie e voti (liste di interi), restituisca per ogni materia il voto massimo ottenuto da qualsiasi studente.
'''

# Esercizio 05
# Titolo: "Voto massimo per materia"

'''
Traccia:
Definisci una funzione:
def voto_massimo_per_materia(studenti: dict[str, dict[str, list[int]]]) -> dict[str, int]:

Che restituisca un dizionario con chiavi le materie e valori il voto massimo 
ottenuto in quella materia, considerando tutti gli studenti.

Suggerimenti:
* Per ogni studente, per ogni materia, esamina tutti i voti.
* Aggiorna il voto massimo per la materia se trovi un voto più alto.
* Ricorda di considerare liste vuote (che non forniscono voti).
* Puoi usare funzioni built-in come max() con attenzione.
'''

def voto_massimo_per_materia(studenti: dict[str, dict[str, list[int]]]) -> dict[str, int]:

    voti_max = {}

    for materie in studenti.values():
        for materia, voti in materie.items():
            if not voti:
                continue # così salta le liste vuote (no hanno voti)

            voto_max_studente = max(voti)

            # si aggiorna il voto max per materia
            if materia not in voti_max or voto_max_studente > voti_max[materia]:
                voti_max[materia] = voto_max_studente
    
    return voti_max

studenti = {
    "Anna": {"matematica": [28, 30, 25], "storia": [30, 21, 25], "filosofia": [25, 26, 29]},
    "Luca": {"matematica": [18, 29, 30], "storia": [24, 28, 27], "filosofia": [27, 19, 26]},
    "Marta": {"matematica": [22, 23, 25], "storia": [19, 21, 0], "filosofia": []},
}

print(voto_massimo_per_materia(studenti))


