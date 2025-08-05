'''
Tema: Comprensioni con dizionari annidati
Obiettivo: Estrarre e trasformare dati da strutture complesse
'''

# Esercizio 01
# Titolo: "Estrai studenti promossi"

'''
Traccia:
Hai una struttura dati del tipo:

studenti = {
    "Anna": {"matematica": 28, "storia": 30},
    "Luca": {"matematica": 18, "storia": 24},
    "Marta": {"matematica": 22, "storia": 19},
}

Scrivi una funzione estrai_promossi(studenti: dict, soglia: int = 21) -> list[str] che restituisce 
una lista di nomi di studenti che hanno superato la soglia in tutte le materie.

Esempio: con soglia 21, il risultato dev’essere ["Anna"]

Suggerimento
Usa una list comprehension con:

 * .items() per scorrere il dizionario esterno,

 * all(...) per verificare se tutti i voti superano la soglia.
'''

def estrai_promossi(studenti: dict[str, dict[str, int]], soglia: int) -> list[str]:
    return [studente for studente, voti in studenti.items() if all(voto > soglia for voto in voti.values())]



studenti = {
    "Anna": {"matematica": 28, "storia": 30},
    "Luca": {"matematica": 18, "storia": 24},
    "Marta": {"matematica": 22, "storia": 19},
}

print(estrai_promossi(studenti, 21))



def estrai_promossi(studenti: dict[str, dict[str, int]], materia: str, soglia: int) -> list[str]:
    return [studente for studente, voti in studenti.items() if voti.get(materia, 0) > soglia]

studenti = {
    "Anna": {"matematica": 28, "storia": 30},
    "Luca": {"matematica": 18, "storia": 24},
    "Marta": {"matematica": 22, "storia": 19},
}

print(estrai_promossi(studenti, "storia", 21))
print(estrai_promossi(studenti, "matematica", 21))
print(estrai_promossi(studenti, "fisica", 21))