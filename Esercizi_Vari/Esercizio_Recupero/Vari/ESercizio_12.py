'''
Esercizio: Funzione analyze_strings

Tema: Analisi di una lista di stringhe

Obiettivo:
Dati in input una lista di stringhe, la funzione deve restituire un dizionario con informazioni 
sulle stringhe: lunghezze e ordine alfabetico.

Nome dell’esercizio: analyze_strings

Traccia:
Scrivi una funzione con il seguente header:

def analyze_strings(strings: list[str]) -> dict[str, str]:


La funzione deve restituire un dizionario con quattro chiavi:

"shortest" → la stringa più corta della lista

"longest" → la stringa più lunga della lista

"first_alphabetically" → la stringa che viene prima in ordine alfabetico

"last_alphabetically" → la stringa che viene ultima in ordine alfabetico

Vincoli:

Non usare funzioni built-in come min(), max(), sorted() o simili.

Non usare librerie esterne.

Se la lista è vuota, solleva un’eccezione ValueError con messaggio "lista vuota".

Suggerimento:

Itera manualmente sulla lista per confrontare lunghezze e valori alfabetici.

Puoi inizializzare le variabili con il primo elemento della lista per cominciare i confronti.
'''

def analyze_strings(strings: list[str]) -> dict[str, str]:
    if not strings:
        raise ValueError("lista vuota")
    
    dict_strings = {}
    stringa_corta = strings[0]
    stringa_lunga = strings[0]
    stringa_prima = strings[0]
    stringa_ultima = strings[0]

    for stringa in strings:
        if len(stringa) < len(stringa_corta):
            stringa_corta = stringa
        
        if len(stringa) > len(stringa_lunga):
            stringa_lunga = stringa
        
        if stringa < stringa_prima:
            stringa_prima = stringa
        
        if stringa > stringa_ultima:
            stringa_ultima = stringa
    
    dict_strings["shortest"] = stringa_corta
    dict_strings["longest"] = stringa_lunga
    dict_strings["first_alphabetically"] = stringa_prima
    dict_strings["last_alphabetically"] = stringa_ultima

    return dict_strings

strings = ["banana", "kiwi", "mela", "ananas"]
print(analyze_strings(strings))