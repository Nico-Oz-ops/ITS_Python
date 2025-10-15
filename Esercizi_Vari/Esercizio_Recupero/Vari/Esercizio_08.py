'''
Esercizio: Funzione compute_lengths

Scrivi una funzione con il seguente header:

* compute_lengths(strings: list[str]) -> dict[str, float]

che, data una lista di stringhe, ritorni un dizionario con tre chiavi:

    * "shortest" -> lunghezza della stringa più corta
    * "longest" -> lunghezza della stringa più lunga
    * "average" -> lunghezza media delle stringhe (somma delle lunghezze diviso numero di stringhe)

Se la lista è vuota, solleva un'eccezione ValueError con messaggio "lista vuota".

Vincolo:
I valori di "shortest", "longest" e "average" non possono essere calcolati usando 
funzioni built-in come min(), max() o sum(), né altre librerie esterne.
'''

def compute_lengths(strings: list[str]) -> dict[str, float]:
    if not strings:
        raise ValueError("lista vuota")
    
    dict_strings = {}
    lunghezza_min = len(strings[0])
    lunghezza_max = len(strings[0])
    somma_lunghezze = 0

    for stringa in strings:
        lunghezza = len(stringa)
        somma_lunghezze += lunghezza

        if lunghezza < lunghezza_min:
            lunghezza_min = lunghezza
        
        if lunghezza > lunghezza_max:
            lunghezza_max = lunghezza
    
    media_lunghezze = somma_lunghezze / len(strings)

    dict_strings["shortest"] = lunghezza_min
    dict_strings["longest"] = lunghezza_max
    dict_strings["average"] = media_lunghezze

    return dict_strings