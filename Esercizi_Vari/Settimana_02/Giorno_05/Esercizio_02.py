'''
Tema: Ricorsione su stringa
Obiettivo: Rimuovere i caratteri duplicati consecutivi in una stringa.
'''

# Esercizio 02
# Titolo: "rimuovi_doppie"

'''
Traccia:
Scrivi una funzione ricorsiva che prende una stringa e restituisce 
una nuova stringa in cui sono rimossi tutti i caratteri duplicati consecutivi.

Suggerimento:
Confronta il primo carattere con il successivo per decidere se 
includerlo o saltarlo, poi ricorri sul resto.
'''

def rimuovi_doppie(s: str) -> str:
    if len(s) <= 1:
        return s
    
    if s[0] != s[1]:
        return s[0]+ rimuovi_doppie(s[1:])
    
    else:
        return rimuovi_doppie(s[1:])

    
print(rimuovi_doppie("pizzapizzaiolo"))

















