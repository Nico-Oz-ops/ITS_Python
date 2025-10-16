'''
Titolo dell’esercizio:
Analisi delle altezze delle persone
 
Obiettivo:
Data in input una lista di dizionari contenenti informazioni su persone, ognuna con nome e altezza 
in centimetri (espressa come float), la funzione deve restituire un dizionario con le seguenti informazioni:
- Il nome della persona più alta
- Il nome della persona più bassa
- L’altezza media
 
Header della funzione: 
def analyze_heights(people: list[dict[str, float]]) -> dict[str, any]:
 
Struttura della lista in input:
Ogni dizionario della lista avrà questa struttura:
{"nome": str, "altezza": float}
 
Requisiti:
* Non usare funzioni già pronte come min(), max(), sorted(), sum(), statistics o simili
* Non usare librerie esterne
* Se la lista è vuota, solleva ValueError("lista vuota")
'''

from typing import Any

def analyze_heights(people: list[dict[str, float]]) -> dict[str, Any]:
    if not people:
        raise ValueError("Lista vuota")
    
    persona_alta_nome = people[0]["nome"]
    persona_bassa_nome = people[0]["nome"]
    persona_alta_altezza = people[0]["altezza"]
    persona_bassa_altezza = people[0]["altezza"]    
    somma_altezza = 0
    dict_persone = {}

    for persona in people:
        altezza = persona["altezza"]

        if altezza > persona_alta_altezza:
            persona_alta_altezza = float(altezza)
            persona_alta_nome = persona["nome"]
        
        if altezza < persona_bassa_altezza:
            persona_bassa_altezza = float(altezza)
            persona_bassa_nome = persona["nome"]
        
        somma_altezza += altezza
    
    media_altezza = somma_altezza / len(people)

    dict_persone["nome del più alto"] = persona_alta_nome
    dict_persone["nome del più basso"] = persona_bassa_nome
    dict_persone["altezza media"] = float(media_altezza)

    return dict_persone

persone = [
    {"nome": "Luca", "altezza": 175.0},
    {"nome": "Anna", "altezza": 160.5},
    {"nome": "Marco", "altezza": 182.3},
    {"nome": "Giulia", "altezza": 168.2}
]

print(analyze_heights(persone))