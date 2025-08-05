'''
Tema: Ricorsione semplice
Obiettivo: Riscrivere la funzione per verificare se una stringa è palindroma, 
senza usare slicing, ma usando la ricorsione con due indici (inizio e fine).
'''

# Esercizio 02
# Titolo: "Verifica se una stringa è palindroma (versione con indici)"

'''
Traccia:
Scrivi una funzione ricorsiva che restituisce True 
se la sottostringa delimitata dagli indici inizio e fine (incluso) è palindroma, False altrimenti.

Suggerimento:
Caso base: se inizio >= fine → la stringa (o sottostringa) è palindroma.
Se s[inizio] != s[fine] → non è palindroma.
Altrimenti richiama la funzione su inizio + 1 e fine - 1.
'''

def is_palindroma_indici(s: str, inizio: int, fine: int) -> bool:
    if inizio >= fine:
        return True
    
    if s[inizio] != s[fine]:
        return False
    
    return is_palindroma_indici(s, inizio + 1, fine -1)

def is_palindroma(s: str) -> bool:
    return is_palindroma_indici(s, 0, len(s) - 1)

print(is_palindroma("ana"))
print(is_palindroma("oro"))
print(is_palindroma("javier"))
print(is_palindroma(""))
























