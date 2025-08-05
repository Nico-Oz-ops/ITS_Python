'''
Tema: Approccio funzionale su dati testuali
Obiettivo: Applicare map, filter, lambda e comprehension su stringhe
'''

# Esercizio 05
# Titolo: "Parole con lunghezza pari trasformate in maiuscolo"

'''
Traccia
Scrivi una funzione che prende in input una lista di stringhe e:

* Filtra solo le parole che hanno lunghezza pari
* Trasforma tutte le parole selezionate in maiuscolo
* Restituisce la nuova lista di parole

Suggerimento
Puoi usare:

* filter con lambda parola: len(parola) % 2 == 0
* map con lambda parola: parola.upper()
* Oppure tutto in una list comprehension

Esempio:
trasforma_parole(["cane", "gatto", "elefante", "orso", "topo", "gufo"])
['CANE', 'ORSO', 'TOPO']
'''

def trasforma_parole(parole: list[str]) -> list[str]:

    parole_lunghezza_pari = filter(lambda parola: len(parola) % 2 == 0, parole)
    parole_maiuscolo = map(lambda parola: parola.upper(), parole_lunghezza_pari)
    return list(parole_maiuscolo)

print(trasforma_parole(["cane", "gatto", "elefante", "orso", "topo", "gufo"]))



def trasforma_parole(parole: list[str]) -> list[str]:
    return [parola.upper() for parola in parole if len(parola) % 2 == 0]

print(trasforma_parole(["cane", "gatto", "elefante", "orso", "topo", "gufo"]))


