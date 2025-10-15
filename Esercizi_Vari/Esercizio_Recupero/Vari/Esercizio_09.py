'''
Esercizio: Funzione select_and_join

Scrivi una funzione con il seguente header:

* select_and_join(strings: list[str], min_length: int) -> str

Descrizione:
La funzione prende:

    * una lista di stringhe strings
    * un intero min_length
    * e restituisce una singola stringa concatenando tutte le stringhe di strings 
    la cui lunghezza è maggiore o uguale a min_length, separate da punto e virgola (;).
'''

def select_and_join(strings: list[str], min_length: int) -> str:
    return ";".join(stringa for stringa in strings if len(stringa) >= min_length)

stringhe = ["hola", "como", "va", "?"]
lunghezza_min = 3
print(select_and_join(stringhe, lunghezza_min))

