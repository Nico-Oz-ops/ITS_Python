'''
Tema: Liste di dizionari - Dati annidati per categoria
Obiettivo: Per ogni materia, trovare il voto massimo tra tutti gli studenti.

Nome dell’esercizio: miglior_voto_per_materia

Traccia:
Ogni studente è rappresentato come un dizionario con nome e un sotto-dizionario 
materie dove le chiavi sono i nomi delle materie e i valori sono le liste di voti.
Scrivi una funzione miglior_voto_per_materia che ritorni un dizionario {materia: voto_massimo} 
considerando tutti gli studenti.

Input:
studenti = [
    {"nome": "Marco", "materie": {"matematica": [18, 25], "storia": [28, 30]}},
    {"nome": "Giulia", "materie": {"matematica": [22, 24], "storia": [26, 27]}},
    {"nome": "Elena", "materie": {"matematica": [30, 29], "storia": [25, 26]}},
]

Output atteso: un dizionario del tipo {"matematica": 30, "storia": 30}.

Suggerimento: Puoi iterare su tutti gli studenti e aggiornare il dizionario delle 
materie man mano che trovi voti più alti.
'''
# Alternativa 1
def miglior_voto_per_materia(studenti: list[dict[str, dict[str, list[int]]]]) -> dict[str, int]:
    risultato = {}

    for studente in studenti:
        for materia in studente["materie"]:
            voto_max = max(studente["materie"][materia])
            if materia not in risultato: 
                risultato[materia] = voto_max
            # al posto di if ed elif si poteva aggiungere un or, cioè if materia not in risultato or voto_max > risultato[materia]
            elif voto_max > risultato[materia]:
                risultato[materia] = voto_max
    return risultato            

studenti = [
    {"nome": "Marco", "materie": {"matematica": [18, 25], "storia": [28, 30]}},
    {"nome": "Giulia", "materie": {"matematica": [22, 24], "storia": [26, 27]}},
    {"nome": "Elena", "materie": {"matematica": [30, 29], "storia": [25, 26]}},
]

print(miglior_voto_per_materia(studenti))

# Alternativa 2
def miglior_voto_per_materia(studenti: list[dict[str, dict[str, list[int]]]]) -> dict[str, int]:
    # aggiungo ogni materia al set (set comprehension), così alla fine ottengo tutte le materie presenti 
    # in tutti gli studenti, senza duplicati.
    # for studente in studenti → scorre tutti gli studenti nella lista. (ciclo esterno)
    # for m in studente["materie"] → scorre tutte le chiavi (materie) nel dizionario materie di quello studente. (ciclo interno)
    materie = set(materia for studente in studenti for materia in studente["materie"])

    return {materia: max(voto for studente in studenti
                         for voto in studente["materie"].get(materia, []))
                         for materia in materie}

studenti = [
    {"nome": "Marco", "materie": {"matematica": [18, 25], "storia": [28, 25]}},
    {"nome": "Giulia", "materie": {"matematica": [22, 24], "storia": [26, 27]}},
    {"nome": "Elena", "materie": {"matematica": [20, 29], "storia": [25, 26]}},
]

print(miglior_voto_per_materia(studenti))

'''
uso del metodo get():
1. studente["materie"] è un dizionario con chiavi = nomi delle materie e valori = liste di voti.
2. get(materia, []) cerca di ottenere la lista dei voti per la materia specificata.
3. Se la chiave materia esiste, restituisce la lista di voti corrispondente.
4. Se la chiave materia non esiste, restituisce il valore di default [] (lista vuota) invece di generare un errore KeyError.
5. Poi il for voto in ... scorre ciascun voto della lista restituita.
'''
