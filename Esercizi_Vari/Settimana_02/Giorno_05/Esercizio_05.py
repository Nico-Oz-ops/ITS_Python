'''
Tema: Ricorsione su insiemi (set)
Obiettivo: Contare quanti elementi in un set sono stringhe che contengono almeno una vocale
'''

# Esercizio 05
# Titolo: "conta_stringhe_con_vocali"

'''
Traccia:
Scrivi una funzione ricorsiva che prende un set di elementi (di qualsiasi tipo) 
e conta quante stringhe contengono almeno una vocale (a, e, i, o, u, anche maiuscole).
Ignora tutti gli elementi non stringa.

Suggerimento:
* Estrai un elemento dal set con next(iter(...))
* Verifica se è una stringa
* Se sì, controlla se almeno una vocale è presente (puoi usare any(...))
* Richiama la funzione sul resto del set (senza quell'elemento)

Quando hai finito, scrivilo pure e poi procediamo con la versione avanzata con *args, dict comprehension
'''

def conta_stringhe_con_vocali(elementi: set) -> int:
    if len(elementi) == 0:
        return 0
    
    vocali = {"a", "e", "i", "o", "u"}
    elemento = next(iter(elementi))
    resto_elementi = elementi.copy()
    resto_elementi.remove(elemento)

    if isinstance(elemento, str) and any(vocale in elemento.lower() for vocale in vocali):
        return 1 + conta_stringhe_con_vocali(resto_elementi)
    
    else:
        return conta_stringhe_con_vocali(resto_elementi)
    
print(conta_stringhe_con_vocali({'ciao', 'zzz', 'sky', 3, 'AEIOU', True}))
        
