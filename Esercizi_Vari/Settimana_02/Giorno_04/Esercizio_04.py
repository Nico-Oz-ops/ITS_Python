'''
Tema: Ricorsione + stringhe
Obiettivo: Scrivi una funzione ricorsiva inverti_stringa(s: str) -> str 
che prende una stringa e restituisce la stringa invertita.
'''

# Esercizio 04
# Titolo: "Inverti stringa"

'''
Traccia:
La funzione deve restituire la stringa invertita, usando la ricorsione 
senza funzioni built-in tipo reversed() o slicing avanzati come s[::-1].

Suggerimento:
Il caso base è quando la stringa è vuota o di lunghezza 1

Altrimenti prendi l’ultimo carattere e aggiungilo davanti alla ricorsione sulla parte iniziale (es. s[:-1])
'''

def inverti_stringa(s: str) -> str:
    if s == "":
        return ""
    
    if len(s) == 1:
        return s
    
    else:
        return s[-1] + inverti_stringa(s[:-1])

print(inverti_stringa("nicolas"))
