'''
Tema: Ricorsione su stringhe
Obiettivo: Contare quante consonanti sono presenti in una stringa.
'''

# Esercizio 04
# Titolo: "Conta consonanti"

'''
Traccia:
Scrivi una funzione ricorsiva che prende una stringa s e restituisce il numero di consonanti presenti al suo interno.
Le lettere vanno considerate minuscole o maiuscole senza distinzione (quindi trasforma tutto in minuscolo prima di analizzare).

* Le vocali sono: a, e, i, o, u.
* Tutte le lettere alfabetiche diverse da queste sono consonanti.
* Ignora gli spazi e i simboli non alfabetici.

Suggerimento (se serve)
Puoi usare:

* s.lower() per semplificare il confronto
* .isalpha() per ignorare simboli/spazi

Controllare se s[0] è consonante, e poi chiamare la funzione sul resto: s[1:]
'''

def conta_consonanti(stringa: str) -> int:
    if stringa.lower() == "":
        return 0
    
    carattere = stringa[0].lower()
    
    if carattere.isalpha() and carattere not in "aeiou":
        return 1 + conta_consonanti(stringa[1:])
    
    else:
        return conta_consonanti(stringa[1:])

print(conta_consonanti("paralelepipedo"))
    
    
